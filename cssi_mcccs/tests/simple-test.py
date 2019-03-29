#quick test that works on my laptop
from cssi_mcccs import mc_sim as mcs

mySim = mcs.Sim("/home/cbunner/git-repos/MCCCS-ABE/exe-pc/src/topmon")
mySim.runtime.nProc = 4
mySim.io.ltraj = 4
mySim.volume.pmvlmt = [1.0,1.0]
mySim.volume.pmvlmt[1] = 0.5
mySim.init_boxes(2)
mySim.boxes[1].temperature = 400.0
mySim.boxes[1].nchain_mt = [1200,0]
mySim.write_changeLog()
