#quick test that works on my laptop
from cssi_mcccs import mc_sim as mcs

mySim = mcs.Sim("/home/cbunner/git-repos/MCCCS-ABE/exe-pc/src/topmon")
mySim.runtime.nProc = 4
mySim.write_changeLog()
mySim.io.ltraj = 4
mySim.write_errorLog()
mySim.write_changeLog()