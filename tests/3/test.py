from mc3s_pywrapper.readers.read_fort4 import read_fort4
from mc3s_pywrapper.readers.read_topmon import read_topmon


mc_sim = read_topmon("in.topmon.inp", exec_path="")
mc_sim = read_fort4("in.fort.4", mc_sim=mc_sim)

# We aren't pointing to a valid code path, so there should be 1 error
assert len(mc_sim.errorLog) == 1

# Write out the files
mc_sim.write_fort4()
mc_sim.write_topmon()