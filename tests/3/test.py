from mc3s_pywrapper.mc_sim import Sim


mc_sim = Sim.from_inputs("in.topmon.inp", execPath="", fort4="in.fort.4", name="test-3")

# We aren't pointing to a valid code path, so there should be 1 error
assert len(mc_sim.errorLog) == 1

# Write out the files
mc_sim.write_fort4()
mc_sim.write_topmon()
