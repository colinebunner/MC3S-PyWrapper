import f90nml

from mc3s_pywrapper.utilities import string_util as su
from mc3s_pywrapper.utilities.namelist import n2p
from mc3s_pywrapper.chemistry import angle, bond, dihedral, vdW

def read_topmon(file_path, mc_sim):
    '''
        Reads a topmon file into a Sim object

        Input:
            file_path [str, os.path]: Path to topmon.inp file to read.
            mc_sim [Sim]: mc3s_pywrapper.mc_sim.Sim object to 
                write topmon.inp simulation data to.
    '''
        
    # This will grab all namelists, but not sections. Those are special to MCCCS, 
    # so we'll have to read them manually.
    top_namelists = f90nml.read(file_path)

    for nml_var, nml in top_namelists.items():
        # We need to grab the right section of our simulation
        sim_nml = getattr(mc_sim, n2p[nml_var])
        # Need to see if the section is empty to avoid calling items() on an empty namespace
        # NOTE: that if you have duplicate entries in your topmon.inp, this will cause problems.
        if len(nml):
            for var, val in nml.items():
                try:
                    setattr(sim_nml, var, val)
                except ValueError:
                    msg = (
                        f"Failed in reading in your topmon.inp data from the file {file_path}.\n"
                        "This is likely due to one of your entries not matching the allowed "
                        "types for that namelist variable.\n"
                        "If you think this is in error, please contact Colin personally "
                        "or open an issue on the github page."
                    )
                    raise ValueError(msg)
    
    # Now for the custom sections
    with open(file_path, "r") as top:
        top_lines = top.readlines()
        for i, line in enumerate(top_lines):
            # Reading ATOMS section
            if line.startswith("ATOMS"):

                # First, we need to figure out how many there are
                natoms = 0
                ncomment = 0
                while True:
                    if top_lines[i+natoms+ncomment+1].startswith("END"):
                        break
                    elif top_lines[i+natoms+ncomment+1].startswith("!"):
                        ncomment += 1
                    else:
                        natoms += 1

                # Next, we need to know whether ATOMS already exist in this simulation. If so,
                # we won't override them
                if mc_sim.atoms:
                    nexists = len(mc_sim.atoms.data.values())
                    print(
                        "Sim already has {nexists} atom types defined vs {natoms} atom types found here.\n"
                        "I am skipping this section."
                    )
                    continue
                
                # Now, we will read in the atom type data
                mc_sim.init_atoms(natoms)
                inc = 1
                while True:
                    next_line = top_lines[i+inc]
                    if next_line.startswith("END"):
                        break
                    else:
                        try:
                            atom_entry = next_line.split()
                            iunit = int(atom_entry[0])
                            itype = int(atom_entry[1])
                            print(
                                f"Found an atom of vdW type {vdW.vdW_names[itype]} for {inc} unit with identifier {iunit}."
                            )
                            nvdW = vdW.vdW_num_params[itype]
                            vdW_params = [float(v) for v in atom_entry[2:nvdW+2]]
                            q = float(atom_entry[nvdW+2])
                            mass = float(atom_entry[nvdW+3])
                            chemid = atom_entry[nvdW+4]
                            # chname is optional entry
                            try:
                                chname = atom_entry[nvdW+5]
                            except IndexError:
                                chname = None
                            # For better or worse, these lists are indexed starting at 1 for consistency with Fortran
                            new_atype = mc_sim.atoms[inc]
                            new_atype.intID = iunit
                            new_atype.aType = itype
                            new_atype.vdWParams = vdW_params
                            new_atype.charge = q
                            new_atype.mass = mass
                            new_atype.chemID = chemid
                            if chname:
                                new_atype.chName = chname
                            # fin
                            inc += 1
                        except (IndexError, ValueError):
                            msg = f"Failed reading the {inc+1}(st/nd/rd/th) ATOM declaration."
                            raise ValueError(msg)

            # Reading BONDS section 
            if line.startswith("BONDS"):

                # First, we need to figure out how many there are
                nbonds = 0
                ncomment = 0
                while True:
                    if top_lines[i+nbonds+ncomment+1].startswith("END"):
                        break
                    elif top_lines[i+nbonds+ncomment+1].startswith("!"):
                        ncomment += 1
                    else:
                        nbonds += 1

                # Next, we need to know whether BONDS already exist in this simulation. If so,
                # we won't override them
                if mc_sim.bonds:
                    nexists = len(mc_sim.bonds.data.values())
                    print(
                        "Sim already has {nexists} bond types defined vs {nbonds} atom types found here.\n"
                        "I am skipping this section."
                    )
                    continue
                
                # Now, we will read in the atom type data
                mc_sim.init_bonds(nbonds)
                inc = 1
                while True:
                    next_line = top_lines[i+inc]
                    if next_line.startswith("END"):
                        break
                    else:
                        try:
                            bond_entry = next_line.split()
                            iunit = int(bond_entry[0])
                            itype = int(bond_entry[1])
                            print(
                                f"Found a bond of type {bond.bond_names[itype]} for {inc} unit with identifier {iunit}."
                            )
                            nparam = bond.bond_num_params[itype]
                            bond_params = [float(v) for v in bond_entry[2:nparam+2]]

                            # minimumRegrow and maximumRegrow are optional variables for CBMC simulations with
                            # flexible bonds.
                            try:
                                minReg = float(bond_entry[nparam+2])
                            except IndexError:
                                minReg = None
                            try:
                                maxReg = float(bond_entry[nparam+3])
                            except IndexError:
                                maxReg = None

                            # For better or worse, these lists are indexed starting at 1 for consistency with Fortran
                            new_btype = mc_sim.bonds[inc]
                            new_btype.intID = iunit
                            new_btype.bType = itype
                            new_btype.bondParams = bond_params
                            if minReg:
                                new_btype.minimumRegrow = minReg
                            if maxReg:
                                new_btype.maximumRegrow = maxReg
                            # fin
                            inc += 1
                        except (IndexError, ValueError):
                            msg = f"Failed reading the {inc+1}(st/nd/rd/th) BOND declaration."
                            raise ValueError(msg)

            # Reading ANGLES section 
            if line.startswith("ANGLES"):

                # First, we need to figure out how many there are
                nangles = 0
                ncomment = 0
                while True:
                    nl = top_lines[i+nangles+ncomment+1]
                    if nl.startswith("END"):
                        break
                    elif nl.startswith("!"):
                        ncomment += 1
                    else:
                        nangles += 1

                # Next, we need to know whether ANGLES already exist in this simulation. If so,
                # we won't override them
                if mc_sim.angles:
                    nexists = len(mc_sim.angles.data.values())
                    print(
                        "Sim already has {nexists} angle types defined vs {nangles} atom types found here.\n"
                        "I am skipping this section."
                    )
                    continue
                
                # Now, we will read in the atom type data
                mc_sim.init_angles(nangles)
                inc = 1
                while True:
                    next_line = top_lines[i+inc]
                    if next_line.startswith("END"):
                        break
                    else:
                        try:
                            angle_entry = next_line.split()
                            iunit = int(angle_entry[0])
                            itype = int(angle_entry[1])
                            print(
                                f"Found an angle of type {angle.angle_names[itype]} for {inc} unit with identifier {iunit}."
                            )
                            nparam = angle.angle_num_params[itype]
                            angle_params = [float(v) for v in angle_entry[2:nparam+2]]

                            # For better or worse, these lists are indexed starting at 1 for consistency with Fortran
                            new_atype = mc_sim.angles[inc]
                            new_atype.intID = iunit
                            new_atype.aType = itype
                            new_atype.angleParams = angle_params
                            # fin
                            inc += 1
                        except (IndexError, ValueError):
                            msg = f"Failed reading the {inc+1}(st/nd/rd/th) ANGLE declaration."
                            raise ValueError(msg)

            # Reading DIHEDRAL section 
            if line.startswith("DIHEDRALS"):

                # First, we need to figure out how many there are
                ndih = 0
                ncomment = 0
                while True:
                    nl = top_lines[i+ndih+ncomment+1]
                    if nl.startswith("END"):
                        break
                    elif nl.startswith("!"):
                        ncomment += 1
                    else:
                        ndih += 1

                # Next, we need to know whether DIHEDRALS already exist in this simulation. If so,
                # we won't override them
                if mc_sim.dihedrals:
                    nexists = len(mc_sim.dihedrals.data.values())
                    print(
                        "Sim already has {nexists} dihedral types defined vs {ndih} atom types found here.\n"
                        "I am skipping this section."
                    )
                    continue
                
                # Now, we will read in the atom type data
                mc_sim.init_dihedrals(ndih)
                inc = 1
                while True:
                    next_line = top_lines[i+inc]
                    if next_line.startswith("END"):
                        break
                    else:
                        try:
                            dih_entry = next_line.split()
                            iunit = int(dih_entry[0])
                            itype = int(dih_entry[1])
                            print(
                                f"Found a dihedral of type {dihedral.dihedral_names[itype]} for {inc} unit with identifier {iunit}."
                            )
                            nparam = dihedral.dihedral_num_params[itype]
                            dih_params = [float(v) for v in dih_entry[2:nparam+2]]

                            # For better or worse, these lists are indexed starting at 1 for consistency with Fortran
                            new_atype = mc_sim.dihedrals[inc]
                            new_atype.intID = iunit
                            new_atype.dType = itype
                            new_atype.vtt = dih_params
                            # fin
                            inc += 1
                        except (IndexError, ValueError):
                            msg = f"Failed reading the {inc+1}(st/nd/rd/th) DIHEDRAL declaration."
                            raise ValueError(msg)

    return mc_sim