#quick test that works on my laptop
from cssi_mcccs.classes import mc_simulation as mcsim

mySim = mcsim.Sim("/home/cbunner/git-repos/MCCCS-ABE/exe-pc/src/topmon")
mySim.runtime.nProc = 4
mySim.write_changeLog()
mySim.io.ltraj = 4
mySim.write_errorLog()
mySim.write_changeLog()
