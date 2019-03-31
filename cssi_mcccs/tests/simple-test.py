#quick test that works on my laptop
from cssi_mcccs import mc_sim as mcs

# 
mySim = mcs.Sim("/home/cbunner/git-repos/MCCCS-ABE/exe-pc/src/topmon")

# io namelist
mySim.io.ltraj       = True
mySim.L_movie_xyz    = False
mySim.L_movie_pdb    = False
mySim.outputLocation = "file"
mySim.file_run       = "mcrun.dat"
mySim.file_movie     = "movie.dat"
mySim.file_input     = "fort.4"
mySim.file_restart   = "fort.77"
mySim.file_traj      = "fort.12"

# runtime info
mySim.runtime.nProc   = 1
mySim.nThreadsPerProc = 1

# system namelist
mySim.system.lnpt   = False
mySim.system.lgibbs = True
mySim.system.lgrand = False
mySim.system.lanes  = False
mySim.system.ldielect = False


# Volume namelist
mySim.volume.pmvlmt = [1.0,1.0]
mySim.volume.pmvlmt[1] = 0.5

mySim.init_boxes(2)
mySim.boxes[1].temperature = 400.0
mySim.boxes[1].nchain_mt = [1200,0]
mySim.write_changeLog()
