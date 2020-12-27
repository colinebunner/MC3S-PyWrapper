import f90nml

from mc3s_pywrapper.utilities import string_util as su
from mc3s_pywrapper.mc_sim import Sim

def read_fort4(file_path, mc_sim=None, exec_path=None, sim_name=None, skip_exec=False):
    '''
        Reads a fort.4 file and creates a simulation object, if none is passed in. 
        If a simulation isn't passed in, you must pass in a path to a working
        MCCCS-MN executable. I may relax that constraint at some point, as you may
        have a legitimate need to read/write input files without caring about the
        executable. For now, though, this is mandatory.

        Input:
            file_path [str, os.path]: Path to fort.4 file to read.
            mc_sim [Optional[Sim]]: mc3s_pywrapper.mc_sim.Sim object to 
                write fort.4 simulation data to.
            exec_path [Optional[str, os.path]]: Path to a working MCCCS-MN
                executable to use for this project.
            sim_name [Optional[str]]: Optional str name to pass to the Sim()
                constructor. If a previous simulation is passed in, this
                will be ignored.
            skip_exec [Optional[bool]]: Unsupported for now.
    '''

    if mc_sim is None:
        # May relax assertion later
        if exec_path is None:
            raise ValueError(
                "Cannot read fort.4 to a simulation object without specifying the"+
                "object or a path to a working MCCCS-MN executable."
            )
        # If you want to give your Sim "name" field something other than the default,
        # let's pass it in.
        if sim_name:
            mc_sim = Sim(exec_path, name=sim_name)
        else:
            mc_sim = Sim(exec_path)
    else:
        assert isinstance(mc_sim, Sim)


    # This will grab all namelists, but not sections. Those are special to MCCCS, 
    # so we'll have to read them manually.
    f4_namelists = f90nml.read(file_path)

    for nml_var, nml in f4_namelists.items():
        # We need to grab the right section of our simulation
        