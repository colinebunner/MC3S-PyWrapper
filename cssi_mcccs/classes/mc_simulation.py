# Started": 2/02/19 by Colin Bunner
# Basic idea is to treat an MCCCS-MN Monte Carlo simulation as an object. Then getters and setters
# can be used to appropriately work with input files," runs can be aggregated," standardized validation
# can be applied," etc...
import subprocess
import shlex
import os
import sys
import traceback

# Information about executable
class Code:

  def __init__(self,exDir):

    getCodeInfo = "{} -v".format(exDir)
    args = shlex.split(getCodeInfo)
    try:
      version = subprocess.Popen(args,stdout=subprocess.PIPE)
      for i,line in enumerate(version.stdout):
        cl = line.decode("utf-8").strip().split()
        if i==1:
          self.__gitBranch = cl[-1][0:-1]
        elif i==2:
          self.__gitHash = cl[-1]
        elif i==3:
          self.__buildHost = cl[-1]
        elif i==4:
          self.__preprocDefs = cl[-1].split(";")
        elif i==5:
          self.__compilerLocation = cl[-1]
      self.executablePath = exDir
    # Executable not found likely
    except (subprocess.CalledProcessError, OSError) as e:
      print("Shoot")

  @property
  def executablePath(self):
    return self.__executablePath

  @property
  def gitBranch(self):
    return self.__gitBranch

  @property
  def gitHash(self):
    return self.__gitHash

  @property
  def buildHost(self):
    return self.__buildHost

  @property
  def preprocDefs(self):
    return self.__preprocDefs

  @property
  def compilerLocation(self):
    return self.__compilerLocation

  @executablePath.setter
  def executablePath(self,val):
    # Test code by trying to output version before accepting executable path change
    testCode = "{} -v".format(val)
    args = shlex.split(testCode)
    try:
      version = subprocess.check_output(args)
      self.__executablePath = val
    except (subsystem.CalledProcessError,OSError) as e:
      print("Shoot")

# Runtime information
class Run:

  def __init__(self,nproc=None,ntpp=None):

    self.__nProc = nproc
    self.__nThreadsPerProc = ntpp

  @property
  def nProc(self):
    return self.__nProc

  @property
  def nThreadsPerProc(self):
    return self.__nThreadsPerProc

  @nProc.setter
  def nProc(self,nproc):
    self.__nProc = nproc

  @nThreadsPerProc.setter
  def nThreadsPerProc(self,nptt):
    self.__nThreadsPerProc = nptt

# Simulation io control
class IO:

  def __init__(self,file_input="fort.4",file_restart="fort.77",file_struct="input_struct.xyz",file_run="run1a.dat",
                    file_movie="movie1a.dat",file_solute="solute.dat",file_traj="fort.12",outputLocation="file",
                    run_num=1,suffix="a",L_movie_xyz=None,L_movie_pdb=None,file_cbmc_bend="cbmc_bend_table.dat",
                    checkpoint_interval=None,checkpoint_copies=None,use_checkpoint=None,ltraj=None):

    self.__file_input          = file_input
    self.__file_restart        = file_restart
    self.__file_struct         = file_struct
    self.__file_run            = file_run
    self.__file_movie          = file_movie
    self.__file_solute         = file_solute
    self.__file_traj           = file_traj
    self.__outputLocation      = outputLocation
    self.__run_num             = run_num
    self.__suffix              = suffix
    self.__L_movie_xyz         = L_movie_xyz
    self.__L_movie_pdb         = L_movie_pdb
    self.__file_cbmc_bend      = file_cbmc_bend
    self.__ltraj               = ltraj
    if (outputLocation.upper()=="FILE"):  # Rather have users choose "screen" or "terminal" than 2 or 6 like MCCCS
      self.__io_output = 2
    elif (outputLocation.upper()=="TERMINAL"):
      self.__io_output = 6
    else:
      print("Error in instantiation of class IO. outputLocation option not understood.")

  @property
  def file_input(self):
    return self.__file_input

  @property
  def file_restart(self):
    return self.__file_restart

  @property
  def file_struct(self):
    return self.__file_struct

  @property
  def file_run(self):
    return self.__file_run

  @property
  def file_movie(self):
    return self.__file_movie

  @property
  def file_solute(self):
    return self.__file_solute

  @property
  def file_traj(self):
    return self.__file_traj

  @property
  def outputLocation(self):
    return self.__outputLocation

  @property
  def io_output(self):
    return self.__io_output

  @property
  def run_num(self):
    return self.__run_num

  @property
  def suffix(self):
    return self.__suffix

  @property
  def L_movie_xyz(self):
    return self.__L_movie_xyz

  @property
  def L_movie_pdb(self):
    return self.__L_movie_pdb

  @property
  def file_cbmc_bend(self):
    return self.__L_movie_pdb

  @property
  def checkpoint_interval(self):
    return self.__checkpoint_interval

  @property
  def checkpoint_copies(self):
    return self.__checkpoint_copies

  @property
  def use_checkpoint(self):
    return self.__use_checkpoint

  @property
  def ltraj(self):
    return self.__ltraj

  @file_input.setter
  def file_input(self,val):
    self.__file_input=str(val)

  @file_restart.setter
  def file_restart(self,val):
    self.__file_restart=str(val)

  @file_struct.setter
  def file_struct(self,val):
    self.__file_struct=str(val)

  @file_run.setter
  def file_run(self,val):
    self.__file_run=str(val)

  @file_movie.setter
  def file_movie(self,val):
    self.__file_movie=str(val)

  @file_solute.setter
  def file_solute(self,val):
    self.__file_solute=str(val)

  @file_traj.setter
  def file_traj(self,val):
    self.__file_traj=str(val)

  @outputLocation.setter
  def outputLocation(self,val):
    if val.upper() in ["FILE","TERMINAL"]:
      self.__outputLocation=val.upper()
    else:
      print("Error setting outputLocation. Desired option not understood.")

  @run_num.setter
  def run_num(self,val):
    if isinstance(val,int):
      self.__run_num=val
    else:
      print("Error setting run_num. Must be an integer.")
      raise TypeError

  @suffix.setter
  def suffix(self,val):
    self.__suffix=str(val)

  @L_movie_xyz.setter
  def L_movie_xyz(self,val):
    if isinstance(val,bool):
      self.__L_movie_xyz=val
    else:
      print("Error setting L_movie_xyz. Must be a boolean.")
      raise TypeError

  @L_movie_pdb.setter
  def L_movie_pdb(self,val):
    if isinstance(val,bool):
      self.__L_movie_pdb=val
    else:
      print("Error setting L_movie_pdb. Must be a boolean.")
      raise TypeError

  @file_cbmc_bend.setter
  def file_cbmc_bend(self,val):
    self.__file_cbmc_bend=str(val)

  @ltraj.setter
  def ltraj(self,val):
    if isinstance(val,bool):
      self.__ltraj=val
    else:
      print("Error setting ltraj. Must be a boolean.")
      raise TypeError

# Information for writing simulation checkpoint files. Note that this is in the same namelist as io in MCCCS,
# but the save file is notoriously unreliable and I don't want users to worry about it unless they have to.
# I plan to implement more robust ways of handling runtime errors within the Signac framework.
class Checkpoint:

  def __init__(self,allowCheckpoint=False,checkpoint_interval=None,checkpoint_copies=None,use_checkpoint=None):

    #allowCheckpoint controls whether or not the checkpoint file is ever written out
    self.__use_checkpoint      = use_checkpoint
    if allowCheckpoint:
      self.__checkpoint_interval = checkpoint_interval
      self.__checkpoint_copies   = checkpoint_copies
    else:
      # Write checkpoint every 8 days
      self.__checkpoint_interval = 691200.0E0
      self.__checkpoint_copies   = 1

  @property
  def allowCheckpoint(self):
    return self.__allowCheckpoint

  @property
  def checkpoint_interval(self):
    return self.__checkpoint_interval

  @property
  def checkpoint_copies(self):
    return self.__checkpoint_copies

  @property
  def use_checkpoint(self):
    return self.__use_checkpoint

  @allowCheckpoint.setter
  def allowCheckpoint(self,val):
    if not isinstance(val,bool):
      print("Warning in class Checkpoint: new allowCheckpoint is not a boolean. Overwrite rejected.")
    else:
      self.__allowCheckpoint = val

  @checkpoint_interval.setter
  def checkpoint_interval(self,val):
    if not (isinstance(val,float) or isintance(val,int)):
      print("Warning in class Checkpoint: checkpoint_interval must be a number. Overwrite rejected.")
    else:
      self.__checkpoint_interval = float(val)

  @checkpoint_copies.setter
  def checkpoint_copies(self,val):
    if not (isinstance(val,int)):
      print("Warning in class Checkpoint: checkpoint_copies must be an integer. Overwrite rejected.")
    else:
      self.__checkpoint_copies = val

class System:

  def __init__(self,lnpt=None,lgibbs=None,lgrand=None,losmotic_nvt=None,lanes=None,lpbc=None,lpbcx=None,lpbcy=None,
                    lpbcz=None,lfold=None,lexzeo=None,lslit=None,lgraphite=None,lsami=None,lmuir=None,lelect_field=None,
                    lgaro=None,lionic=None,lkdtree=None):

    self.__lnpt         = lnpt
    self.__lgibbs       = lgibbs
    self.__lgrand       = lgrand
    self.__losmotic_nvt = losmotic_nvt
    self.__lanes        = lanes
    self.__lpbc         = lpbc
    self.__lpbcx        = lpbcx
    self.__lpbcy        = lpbcy
    self.__lpbcz        = lpbcz
    self.__lfold        = lfold
    self.__lexzeo       = lexzeo
    self.__lslit        = lslit
    self.__lgraphite    = lgraphite
    self.__lsami        = lsami
    self.__lmuir        = lmuir
    self.__lelect_field = lelect_field
    self.__lgaro        = lgaro
    self.__lionic       = lionic

  @property
  def lnpt(self):
    return self.__lnpt
 
  @property
  def lgibbs(self):
    return self.__lgibbs

  @property
  def lgrand(self):
    return self.__lgrand

  @property
  def losmotic_nvt(self):
    return self.__losmotic_nvt
   
  @property
  def lanes(self):
    return self.__lanes

  @property
  def lpbc(self):
    return self.__lpbc

  @property
  def lpbcx(self):
    return self.__lpbcx

  @property
  def lpbcy(self):
    return self.__lpbcy

  @property
  def lpbcz(self):
    return self.__lpbcz

  @property
  def lfold(self):
    return self.__lfold

  @property
  def lexzeo(self):
    return self.__lexzeo

  @property
  def lslit(self):
    return self.__lslit

  @property
  def lgraphite(self):
    return self.__lgraphite

  @property
  def lsami(self):
    return self.__lsami

  @property
  def lmuir(self):
    return self.__lmuir

  @property
  def lelectric_field(self):
    return self.__lelect_field

  @property
  def lgaro(self):
    return self.__lgaro

  @property
  def lionic(self):
    return self.__lionic

  @lnpt.setter
  def lnpt(self,val):
    if not isinstance(val,bool):
      print("Error setting value for lnpt. Must be a boolean.")
      raise TypeError
    else:
      self.__lnpt=val

  @lgibbs.setter
  def lgibbs(self,val):
    if not isinstance(val,bool):
      print("Error setting value for lgibbs. Must be a boolean.")
      raise TypeError
    else:
      self.__lgibbs=val

  @lgrand.setter
  def lgrand(self,val):
    if not isinstance(val,bool):
      print("Error setting value for lgrand. Must be a boolean.")
      raise TypeError
    else:
      self.__lgrand=val

  @losmotic_nvt.setter
  def losmotic_nvt(self,val):
    if not isinstance(val,bool):
      print("Error setting losmotic_nvt. Must be a boolean.")
      raise TypeError
    else:
      self.__losmotic_nvt=val

  @lanes.setter
  def lanes(self,val):
    if not isinstance(val,bool):
      print("Error setting lanes. Must be a boolean.")
      raise TypeError
    else:
      self.__lanes=val

  @lpbc.setter
  def lpbc(self,val):
    if not isinstance(val,bool):
      print("Error setting lpbc. Must be a boolean.")
      raise TypeError
    else:
      self.__lpbc=val

  @lpbcx.setter
  def lpbcx(self,val):
    if not isinstance(val,bool):
      print("Error setting lpbcx. Must be a boolean.")
      raise TypeError
    else:
      self.__lpbcx=val

  @lpbcy.setter
  def lpbcy(self,val):
    if not isinstance(val,bool):
      print("Error setting lpbcx. Must be a boolean.")
      raise TypeError
    else:
      self.__lpbcy=val

  @lpbcz.setter
  def lpbcz(self,val):
    if not isinstance(val,bool):
      print("Error setting lpbcx. Must be a boolean.")
      raise TypeError
    else:
      self.__lpbcz=val

  @lfold.setter
  def lfold(self,val):
    if not isinstance(val,bool):
      print("Error setting lfold. Must be a boolean.")
      raise TypeError
    else:
      self.__lfold=val

  @lexzeo.setter
  def lexzeo(self,val):
    if not isinstance(val,bool):
      print("Error setting lexzeo. Must be a boolean.")
      raise TypeError
    else:
      self.__lexzeo=val

  @lslit.setter
  def lslit(self,val):
    if not isinstance(val,bool):
      print("Error setting lslit. Must be a boolean.")
      raise TypeError
    else:
      self.__lslit=val

  @lgraphite.setter
  def lgraphite(self,val):
    if not isinstance(val,bool):
      print("Error setting lgraphite. Must be a boolean.")
      raise TypeError
    return self.__lgraphite

  @lsami.setter
  def lsami(self,val):
    if not isinstance(val,bool):
      print("Error setting lsami. Must be a boolean.")
      raise TypeError
    else:
      self.__lsami=val

  @lmuir.setter
  def lmuir(self,val):
    if not isinstance(val,bool):
      print("Error setting lmuir. Must be a boolean.")
      raise TypeError
    else:
      self.__lmuir=val

  @lelectric_field.setter
  def lelectric_field(self,val):
    if not isinstance(val,bool):
      print("Error setting lelectric_field. Must be a boolean.")
      raise TypeError
    else:
      self.__lelect_field=val

  @lgaro.setter
  def lgaro(self,val):
    if not isinstance(val,bool):
      print("Error setting lgaro. Must be a boolean.")
      raise TypeError
    else:
      self.__lgaro=val

  @lionic.setter
  def lionic(self,val):
    if not isinstance(val,bool):
      print("Error setting lionic. Must be a boolean.")
      raise TypeError
    else:
      self.__lionic=val

class MC_Tricks:

  def __init__(self,lcutcm=None,ldual=None,L_Coul_CBMC=None):

    self.__lcutcm       = lcutcm
    self.__ldual        = ldual
    self.__L_Coul_CBMC  = L_Coul_CBMC

  @property
  def lcutcm(self):
    return self.__lcutcm

  @property
  def ldual(self):
    return self.__ldual

  @property
  def L_Coul_CBMC(self):
    return self.__L_Coul_CBMC

  @lcutcm.setter
  def lcutcm(self,val):
    if not isinstance(val,bool):
      print("Error setting lcutcm. Must be a boolean.")
      raise TypeError
    else:
      self.__lcutcm=val

  @ldual.setter
  def ldual(self,val):
    if not isinstance(val,bool):
      print("Error setting ldual. Must be a boolean.")
      raise TypeError
    else:
      self.__ldual=val

  @L_Coul_CBMC.setter
  def L_Coul_CBMC(self,val):
    if not isinstance(val,bool):
      print("Error setting L_Coul_CBMC. Must be a boolean.")
      raise TypeError
    else:
      self.__L_Coul_CBMC=val

class MC_Sim:

  def __init__(self,executable):

    self.code       = Code(executable)

    self.run        = Run()

    self.io         = IO()

    self.checkpoint = Checkpoint()

    self.system     = System()

    self.mc_tricks  = MC_Tricks()

#   todo: lvirial,lmipsw,lexpee,ldielect
    self.system     = {"lijall":None,"lchgall":None,
                       "lewald":None,"lrecip":None,"ltailc":None,"lshift":None,
                       "lneigh":None,"lmixlb":None,"lmixjo":None,"lmixwh":None,"lmixkong":None,
                       "L_spline":None,"L_linear":None,"L_vib_table":None,"L_bend_table":None,"L_elect_table":None,"L_cbmc_bend":None,
                       "lkdtree":None}

    self.mc_shared  = {"seed":1,"nbox":1,"nmolty":1,"nchain":1,"nstep":1,"time_limit":100,"lstop":None,"iratio":300,"rmin":1.0,
                       "softcut":100.0e0,"linit":None,"lreadq":None,"N_add":0,"box2add":1,"moltyp2add":1,"lEqRun":None}

    self.analysis   = {"iprint":1,"imv":1,"iblock":1,"iratp":1,"idiele":1,"iheatcapacity":1,"ianalyze":1,"nbin":1,"lrdf":None,"lintra":None,
                       "lstretch":None,"lgvst":None,"lbend":None,"lete":None,"lrhoz":None,"bin_width":0.2,"lucall":None,"nvirial":1,
                       "starvir":1,"stepvir":1,"ntemp":1,"virtemp":1}

    self.atoms      = {"nAtomTypes":1,"atomID":[],"atomType":{},"atomNBParams":{},"atomCharge":{},"atomMass":{},"atomName":{}}

    self.bonds      = {"nBondTypes":1,"bondID":[],"bondType":{},"bondEqDist":{},"bondForceConst":{}}

    self.angles     = {"nAngleTypes":1,"angleID":[],"angleType":{},"angleEqDist":{},"angleForceConst":{}}

    self.dihedrals  = {"nDihedralTypes":1,"dihedralID":[],"dihedralType":{},"dihedralParams":{}}

    self.mc_volume  = {"tavol":0.3E0,"iratv":10,"pmvlmt":[],"nvolb":1,"pmvolb":[],"box5":[],"box6":[],"pmvol":0.0E0,"pmvolx":0.0E0,
                      "pmvoly":0.0E0,"rmvolume":1.0E0,"allow_cutoff_failure":1}

    self.mc_swatch  = {"pmswat":0.0E0,"nswaty":1,"pmsatc":[]}

    self.mc_swap    = {"pmswap":0.0E0,"pmswmt":[]}

    self.mc_cbmc    = {"rcutin":1.0E0,"pmcb":0.0E0,"pmcbmt":[],"pmall":[],"nchoi1":[],"nchoi":[],"nchoir":[],"nchoih":[],"nchoig":[],
                      "nchtor":[],"nchbna":[],"nchbnb":[],"icbdir":[],"icbsta":[],"rbsmax":1.0E0,"rbsmin":1.0E0,"first_bead_to_swap":1,
                      "avbmc_version":[],"pmbias":[],"pmbsmt":[],"pmbias2":[],"pmfix":[],"pmgroup":[],"lrig":[],"lpresim":None,"iupdatefix":1}

    self.mc_ee      = {"pmexpc":0.0E0,"pmeemt":[],"pmexpc1":0.0E0,"lexpand":[]}

    self.mc_flucq   = {"taflcq":0.3E0,"fqtemp":5.0E0,"rmflucq":1.0E0,"pmflcq":0.0E0,"pmfqmt":[],"lflucq":[],"lqtrans":[],"fqegp":[],"nchoiq":[]}

    self.gcmc       = {"B":[],"nequil":1,"ninstf":1,"ninsth":1,"ndumph":1}

    self.external_field = {"surface_type":1,"ntsubst":1,"rsol":1,"a1":1,"Elect_field":[],"double_surface":[]}

mySim = MC_Sim("/home/cbunner/git-repos/MCCCS-ABE/exe-pc/src/topmon")
