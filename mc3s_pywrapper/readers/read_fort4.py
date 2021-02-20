import f90nml

from mc3s_pywrapper.utilities import string_util as su
from mc3s_pywrapper.utilities.namelist import n2p

def nextline(lines, start):
    counter = 0
    while True:
        next_line = lines[start+counter]
        if next_line.startswith("!"):
            counter += 1
        else:
            break

    return next_line, counter

def read_fort4(file_path, mc_sim=None, exec_path=None, sim_name=None, skip_exec=False):
    '''
        Reads data from a fort.4 file into a Sim object

        Input:
            file_path [str, os.path]: Path to fort.4 file to read.
            mc_sim [Sim]: mc3s_pywrapper.mc_sim.Sim object to 
                write fort.4 simulation data to.
    '''

    # This will grab all namelists, but not sections. Those are special to MCCCS, 
    # so we'll have to read them manually.
    f4_namelists = f90nml.read(file_path)

    for nml_var, nml in f4_namelists.items():
        # We need to grab the right section of our simulation
        sim_nml = getattr(mc_sim, n2p[nml_var])
        # Need to see if the section is empty to avoid calling items() on an empty namespace
        # NOTE: that if you have duplicate entries in your fort.4, this will cause problems.
        if len(nml):
            for var, val in nml.items():
                try:
                    setattr(sim_nml, var, val)
                except (AttributeError, ValueError) as e:
                    raise AttributeError(e, 
                        f"Failed in reading in your fort.4 data from the file {file_path}.\n"
                        "This is likely due to one of your entries not matching the allowed "
                        "types for that namelist variable.\n"
                        "If you think this is in error, please contact Colin personally "
                        f"or open an issue on the github page.\nVars: {var}, {val}"
                    )
    
    # Now for the custom sections
    with open(file_path, "r") as f4:
        f4_lines = f4.readlines()
        for i, line in enumerate(f4_lines):

            # Reading SIMULATION_BOX section
            if line.startswith("SIMULATION_BOX"):

                # First, we need to figure out how many there are
                nbox = 0
                ncomment = 0
                while True:
                    if f4_lines[i+nbox+ncomment].startswith("END"):
                        break
                    elif f4_lines[i+nbox+ncomment].startswith("!"):
                        ncomment += 1
                    else:
                        nbox += 1
                # Each box entry takes up three lines
                nbox = int(nbox // 3)

                # Next, we need to know whether boxes already exist in this simulation. If so,
                # we won't override them
                if mc_sim.boxes:
                    nexists = len(mc_sim.boxes.data.values())
                    print(
                        "Sim already has {nexists} simulation boxes defined vs {nbox} simulation boxes found here.\n"
                        "I am skipping this section."
                    )
                    continue
                
                # Now, we will read in the atom type data
                mc_sim.init_boxes(nbox)
                inc = 1
                box_num = 1
                while True:
                    first  = f4_lines[i+inc]
                    if first.startswith("END"):
                        break
                    # Skip comments
                    elif first.startswith("!"):
                        inc += 1
                    else:
                        try:
                            # Grab other two lines associated with this box entry
                            while True:
                                inc += 1
                                second = f4_lines[i+inc]
                                if not second.startswith("!"):
                                    break
                            while True:
                                inc += 1
                                third = f4_lines[i+inc]
                                if not third.startswith("!"):
                                    break
                            blx, bly, blz, rc, kalp, rcnn, niso, lsol, lrec, lid, ltw, t, p = first.split()
                            # Length will depend on the number of each mtype
                            second = second.split()
                            nmty = int(len(second)//2)
                            print(f"Found ininch/ghost_particles for {nmty} molecule types")
                            ininch = second[:nmty]
                            gp = second[-1]
                            inix, iniy, iniz, inirot, inimix, zshift, dshift, ul, rimax = third.split()

                            # For better or worse, these lists are indexed starting at 1 for consistency with Fortran
                            new_box = mc_sim.boxes[box_num]
                            new_box.boxlx = float(blx)
                            new_box.boxly = float(bly)
                            new_box.boxlz = float(blz)
                            new_box.rcut  = float(rc)
                            new_box.kalp  = float(kalp)
                            new_box.rcutnn = float(rcnn)
                            new_box.numDimIso = int(niso)
                            new_box.lsolid = bool(lsol)
                            new_box.lrect = bool(lrec)
                            new_box.lideal = bool(lid)
                            new_box.ltwice = bool(ltw)
                            new_box.T = float(t)
                            new_box.P = float(p)
                            new_box.nchain_mt = [int(v) for v in ininch]
                            new_box.ghost_particles = int(gp)
                            new_box.inix = int(inix)
                            new_box.iniy = int(iniy)
                            new_box.iniz = int(iniz)
                            new_box.inirot = int(inirot)
                            new_box.inimix = int(inimix)
                            new_box.zshift = float(zshift)
                            new_box.dshift = float(dshift)
                            new_box.use_linkcell = bool(ul)
                            new_box.rintramax = float(rimax)
                            box_num += 1
                            inc += 1
                        except (IndexError, ValueError) as e:
                            msg = f"Failed reading the {box_num}(st/nd/rd/th) SIMULATION_BOX declaration."
                            raise ValueError(e, msg)

            # Reading MOLECULE_TYPE section
            if line.startswith("MOLECULE_TYPE"):

                # First, we need to figure out how many moltypes there are
                nmty = 0
                ncomment = 0
                while True:
                    nl = f4_lines[i+ncomment]
                    if nl.startswith("END"):
                        break
                    elif nl.startswith("!"):
                        ncomment += 1
                    elif len(nl.split()) == 15:
                        nmty += 1
                        ncomment += 1
                    else:
                        ncomment += 1


                # Next, we need to know whether mtypes already exist in this simulation. If so,
                # we won't override them.
                if mc_sim.mtypes:
                    nexists = len(mc_sim.mtypes.data.values())
                    print(
                        "Sim already has {nexists} molecule types defined vs {nmty} molecule types found here.\n"
                        "I am skipping this section."
                    )
                    continue
                
                mc_sim.init_mtypes(nmty)
                inc = 1
                mt_num = 1
                while True:
                    first  = f4_lines[i+inc]
                    if first.startswith("END"):
                        break
                    # Skip comments
                    elif first.startswith("!"):
                        inc += 1
                        first = f4_lines[i+inc]
                    else:
                        first = first.split()
                        try:
                            assert len(first) == 15, first
                            nunit, nugrow, ncar, maxcb, maxgr, ir, lel, lring, lrig, lbr, lset, lq, qs, iur, isol = first
                            if bool(lrig):
                                inc += 1
                                nl, cnt = nextline(f4_lines, i+inc)
                                inc += cnt
                                gpoints = nl.split()

                            # We have all the info needed to set up the molecule type now (but not the beads attribute)
                            new_mtype = mc_sim.mtypes[mt_num]
                            new_mtype.nunit = int(nunit)
                            new_mtype.nugrow = int(nugrow)
                            new_mtype.ncarbon = int(ncar)
                            new_mtype.maxcbmc = int(maxcb)
                            new_mtype.maxgrow = int(maxgr)
                            new_mtype.iring = int(ir)
                            new_mtype.lelect = bool(lel)
                            new_mtype.lring = bool(lring)
                            new_mtype.lrigid = bool(lrig)
                            new_mtype.lbranc = bool(lbr)
                            new_mtype.lsetup = bool(lset)
                            new_mtype.lq14scale = bool(lq)
                            new_mtype.qscale = float(qs)
                            new_mtype.iurot = int(iur)
                            new_mtype.isolute = int(isol)

                            # Now for the beads portion
                            new_mtype.init_beads()
                            for iunit in range(int(nunit)):
                                # Reference to bead to populate info for
                                new_bead = new_mtype.beads[iunit + 1]
                                # Grab next uncommmented line, which should be (unit ntype leaderq)
                                # Add to inc the number of commented lines encountered
                                bead_def, cnt = nextline(f4_lines, i+inc)
                                inc += cnt
                                # Pull info, assert that unit matches number based on loop
                                un, nt, lq = bead_def.split()
                                assert int(un) == iunit+1, un
                                new_bead.ntype   = int(nt)
                                new_bead.leaderq = int(lq)

                                # Next should be stretch definition
                                inc += 1
                                nstretch, cnt = nextline(f4_lines, i+inc)
                                inc += cnt
                                nstretch = int(nstretch.split()[0])
                                stretches = []
                                for stretch in range(nstretch):
                                    inc += 1
                                    nl, cnt = nextline(f4_lines, i+inc)
                                    inc += cnt
                                    nl = nl.split()
                                    stretches.append((int(nl[0]), int(nl[1])))
                                new_bead.nbonds = len(stretches)
                                new_bead.init_bonds()
                                new_bead.bonds = stretches
                            
                                # Next should be angle definition
                                inc += 1
                                nbend, cnt = nextline(f4_lines, i+inc)
                                inc += cnt
                                nbend = int(nbend.split()[0])
                                bends = []
                                for bend in range(nbend):
                                    inc += 1
                                    nl, cnt = nextline(f4_lines, i+inc)
                                    inc += cnt
                                    nl = nl.split()
                                    bends.append((int(nl[0]), int(nl[1]), int(nl[2])))
                                new_bead.nangles = len(bends)
                                new_bead.init_angles()
                                new_bead.angles = bends
                            
                                # Next should be dihedral definition
                                inc += 1
                                ndih, cnt = nextline(f4_lines, i+inc)
                                inc += cnt
                                ndih = int(ndih.split()[0])
                                dihs = []
                                for dih in range(ndih):
                                    inc += 1
                                    nl, cnt = nextline(f4_lines, i+inc)
                                    inc += cnt
                                    nl = nl.split()
                                    dihs.append((int(nl[0]), int(nl[1]), int(nl[2]), int(nl[3])))
                                new_bead.ndihedrals = len(dihs)
                                new_bead.init_dihedrals()
                                new_bead.dihedrals = dihs
                                inc += 1

                            mt_num += 1

                        except (IndexError, ValueError) as e:
                            msg = f"Failed reading the {mt_num}(st/nd/rd/th) MOLECULE_TYPE declaration."
                            raise ValueError(e, msg)

            # Reading MC_SWAP section
            if line.startswith("MC_SWAP"):

                # First, we need to figure out how many moltypes there are
                nmty = 0
                inc = 1
                while True:
                    nl, cnt = nextline(f4_lines, i + inc)
                    inc += cnt + 1
                    if nl.startswith("END"):
                        break
                    else:
                        nl = nl.split()
                        nswapb = int(nl[0])
                        for j in range(nswapb):
                            nl, cnt = nextline(f4_lines, i + inc)
                            inc += cnt + 1
                        nmty += 1
                print(f"Found box pair definition(s) for {nmty} molecule types in MC_SWAP")


                # Next, we need to know whether mtypes already exist in this simulation. If so,
                # we won't override them.
                if mc_sim.swap_table:
                    nexists = len(mc_sim.swap_table.data.values())
                    print(
                        "Sim already has {nexists} molecule type swap definitions defined vs {nmty} molecule types defs found here.\n"
                        "I am skipping this section."
                    )
                    continue
                
                mc_sim.init_swap_table(nmty)
                inc = 1
                mt_num = 1
                while True:
                    first  = f4_lines[i+inc]
                    if first.startswith("END"):
                        break
                    # Skip comments
                    elif first.startswith("!"):
                        inc += 1
                        first = f4_lines[i+inc]
                    else:
                        first = first.split()
                        try:
                            nswapb = int(first[0])
                            pmswapb = [float(v) for v in first[1:nswapb+1]]

                            new_mtype = mc_sim.swap_table[mt_num]
                            new_mtype.nswapb = nswapb
                            new_mtype.pmswapb = pmswapb

                            inc += 1

                            box_pairs = []
                            for bp in range(nswapb):
                                nl, cnt = nextline(f4_lines, i+inc)
                                inc += cnt
                                nl = nl.split()
                                box_pairs.append((int(nl[0]), int(nl[1])))
                                inc += 1

                            new_mtype.boxPairs = box_pairs
                            mt_num += 1

                        except (IndexError, ValueError) as e:
                            msg = f"Failed reading the {mt_num}(st/nd/rd/th) MC_SWAP swap declaration."
                            raise ValueError(e, msg)

    return mc_sim