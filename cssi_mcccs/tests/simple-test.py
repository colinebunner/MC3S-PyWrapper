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

# Create 2 atom types
mySim.init_atoms(2)
mySim.atoms[1].intID     = 101
mySim.atoms[1].aType     = 1
mySim.atoms[1].vdWParams = [50.0,2.80]
mySim.atoms[1].charge    = -0.26
mySim.atoms[1].mass      = 12.0e0
mySim.atoms[1].chemID    = "C"
mySim.atoms[1].chName    = "C-CS2"
mySim.atoms[2].intID     = 102
mySim.atoms[2].aType     = 1
mySim.atoms[2].vdWParams = [180.0,3.60]
mySim.atoms[2].charge    = 0.13
mySim.atoms[2].mass      = 32.07e0
mySim.atoms[2].chemID    = "S"
mySim.atoms[2].chName    = "S-CS2"

mySim.init_bonds(1)
mySim.bonds[1].intID     = 201
mySim.bonds[1].bType     = 1
mySim.bonds[1].brvib     = 1.550e0
mySim.bonds[1].brvibk    = 0.0e0

mySim.init_angles(1)
mySim.angles[1].intID    = 301
mySim.angles[1].aType    = 1
mySim.angles[1].brben    = 180.0e0
mySim.angles[1].brbenk   = 0.0e0

### fort.4 stuff
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
mySim.boxes[1].set_boxlengths([47.709 for i in range(3)])
mySim.boxes[1].rcut                    = 14.0e0
mySim.boxes[1].kalp                    = 0.250
mySim.boxes[1].rcutnn                  = 0.0e0
mySim.boxes[1].numDimensionIsIsotropic = 3
mySim.boxes[1].lsolid                  = False
mySim.boxes[1].lrect                   = False
mySim.boxes[1].lideal                  = False
mySim.boxes[1].ltwice                  = False
mySim.boxes[1].temperature             = 178.0
mySim.boxes[1].pressure                = 0.0e0
mySim.boxes[1].nchain_mt               = [1200,0]
mySim.boxes[1].inix                    = 11
mySim.boxes[1].iniy                    = 11
mySim.boxes[1].iniz                    = 11
mySim.boxes[1].inirot                  = 0
mySim.boxes[1].inimix                  = 1
mySim.boxes[1].zshift                  = 0.0e0
mySim.boxes[1].dshift                  = 4.337
mySim.boxes[1].use_linkcell            = False
mySim.boxes[1].rintramax               = 0.0e0

bl = 217.084
mySim.boxes[2].set_boxlengths([bl for i in range(3)])
mySim.boxes[2].rcut                    = bl*0.30
mySim.boxes[2].kalp                    = 0.250
mySim.boxes[2].rcutnn                  = 0.0e0
mySim.boxes[2].numDimensionIsIsotropic = 3
mySim.boxes[2].lsolid                  = False
mySim.boxes[2].lrect                   = False
mySim.boxes[2].lideal                  = False
mySim.boxes[2].ltwice                  = False
mySim.boxes[2].temperature             = 178.0
mySim.boxes[2].pressure                = 0.0e0
mySim.boxes[2].nchain_mt               = [300,0]
mySim.boxes[2].inix                    = 7
mySim.boxes[2].iniy                    = 7
mySim.boxes[2].iniz                    = 7
mySim.boxes[2].inirot                  = 0
mySim.boxes[2].inimix                  = 1
mySim.boxes[2].zshift                  = 0.0e0
mySim.boxes[2].dshift                  = bl/7.0e0
mySim.boxes[2].use_linkcell            = False
mySim.boxes[2].rintramax               = 0.0e0

mySim.init_mtypes(1)
mySim.mtypes[1].nunit     = 3
mySim.mtypes[1].nugrow    = 3
mySim.mtypes[1].ncarbon   = 3
mySim.mtypes[1].maxcbmc   = 3
mySim.mtypes[1].maxgrow   = 3
mySim.mtypes[1].iring     = 3
mySim.mtypes[1].lelect    = True
mySim.mtypes[1].lring     = False
mySim.mtypes[1].lrigid    = False
mySim.mtypes[1].lbranch   = False
mySim.mtypes[1].lsetup    = False
mySim.mtypes[1].lq14scale = False
mySim.mtypes[1].qscale    = 0.5e0
mySim.mtypes[1].iurot     = 0
mySim.mtypes[1].isolute   = 1000000
mySim.mtypes[1].init_beads()
mySim.mtypes[1].beads[1].ntype         = 102
mySim.mtypes[1].beads[1].leaderq       = 1
mySim.mtypes[1].beads[1].nbonds        = 1
mySim.mtypes[1].beads[1].init_bonds()
mySim.mtypes[1].beads[1].bonds         = (2,201)
mySim.mtypes[1].beads[1].nangles       = 1
mySim.mtypes[1].beads[1].init_angles()
mySim.mtypes[1].beads[1].angles        = (2,3,301)
mySim.mtypes[1].beads[1].ndihedrals    = 0
mySim.mtypes[1].beads[2].ntype         = 101
mySim.mtypes[1].beads[2].leaderq       = 2
mySim.mtypes[1].beads[2].nbonds        = 2
mySim.mtypes[1].beads[2].init_bonds()
mySim.mtypes[1].beads[2].bonds         = [(1,201),(3,201)]
mySim.mtypes[1].beads[2].nangles       = 0
mySim.mtypes[1].beads[2].ndihedrals    = 0
mySim.mtypes[1].beads[3].ntype         = 101
mySim.mtypes[1].beads[3].leaderq       = 3
mySim.mtypes[1].beads[3].nbonds        = 1
mySim.mtypes[1].beads[3].init_bonds()
mySim.mtypes[1].beads[3].bonds         = (3,201)
mySim.mtypes[1].beads[3].nangles       = 1
mySim.mtypes[1].beads[3].init_angles()
mySim.mtypes[1].beads[3].angles        = (2,1,301)
mySim.mtypes[1].beads[3].ndihedrals    = 0

mySim.write_changeLog()
