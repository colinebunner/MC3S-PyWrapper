#Example that uses nearly all setters to test for errors in the code
from cssi_mcccs import mc_sim as mcs

#
mySim = mcs.Sim("/home/cbunner/git-repos/MCCCS-ABE/exe-pc/src/topmon")

# runtime info
mySim.runtime.nProc   = 1
mySim.nThreadsPerProc = 1

### topmon.inp

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

# system namelist
mySim.system.lnpt     = False
mySim.system.lgibbs   = True
mySim.system.lgrand   = False
mySim.system.lanes    = False
mySim.system.lvirial  = False
mySim.system.lmipsw   = False
mySim.system.lexpee   = False
mySim.system.ldielect = False
mySim.system.lpbc     = True
mySim.system.lpbcx    = True
mySim.system.lpbcy    = True
mySim.system.lpbcz    = True
mySim.system.lfold    = True
mySim.system.lijall   = False
mySim.system.lchgall  = False
mySim.system.lewald   = True
mySim.system.lcutcm   = True
mySim.system.ltailc   = True
mySim.system.lshift   = False
mySim.system.ldual    = True
mySim.system.L_Coul_CBMC = True
mySim.system.lneigh      = False
mySim.system.lexzeo      = False
mySim.system.lslit       = False
mySim.system.lgraphite   = False
mySim.system.lsami       = False
mySim.system.lmuir       = False
mySim.system.L_Ewald_Auto = True
mySim.system.lmixlb       = True
mySim.system.lmixjo       = False
mySim.system.L_spline            = False
mySim.system.L_linear            = False
mySim.system.L_vib_table         = False
mySim.system.L_bend_table        = False
mySim.system.L_elect_table       = False

# Volume namelist
mySim.volume.tavol  = 0.3e0
mySim.volume.iratv  = 10
mySim.volume.pmvlmt = [1.0e0,1.0e0]
mySim.volume.pmvolb = 1.0e0
mySim.volume.pmvol  = 0.0e0

# Swap namelist
mySim.swap.pmswap = 0.300
mySim.swap.pmswmt = [0.5,1.0]

# CBMC namelist
mySim.cbmc.rcutin = 9.0
mySim.cbmc.pmcb   = 0.0e0
mySim.cbmc.pmcbmt = 1.0e0
mySim.cbmc.nchoi1 = 32
mySim.cbmc.nchoi  = 16
mySim.cbmc.nchoir = 16
mySim.cbmc.nchoih = 1
mySim.cbmc.nchtor = 100
mySim.cbmc.nchbna = 1000
mySim.cbmc.nchbnb = 1000

mySim.init_boxes(2)
mySim.boxes[1].temperature = 400.0
mySim.boxes[1].nchain_mt = [1200,0]

mySim.write_changeLog()
