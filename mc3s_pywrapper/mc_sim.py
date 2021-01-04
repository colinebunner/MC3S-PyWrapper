# Python standard modules
import datetime
import os
import random
import subprocess
import time
# Our module files
from mc3s_pywrapper.utilities import oneDimArray as oda
from mc3s_pywrapper.utilities import objectArray as oba
from mc3s_pywrapper.utilities import dateTools   as dt
from mc3s_pywrapper.utilities import changeLog   as chl
from mc3s_pywrapper.readers   import read_topmon
from mc3s_pywrapper.readers   import read_fort4
from mc3s_pywrapper.writers   import write_topmon as tw
from mc3s_pywrapper.writers   import write_fort4 as fw
# Namelists
import mc3s_pywrapper.sections.code as code
import mc3s_pywrapper.sections.runtime as runtime
import mc3s_pywrapper.sections.io as io
import mc3s_pywrapper.sections.checkpoint as checkpoint
import mc3s_pywrapper.sections.system as system
import mc3s_pywrapper.sections.volume as volume
import mc3s_pywrapper.sections.simple as simple
import mc3s_pywrapper.sections.swap as swap
import mc3s_pywrapper.sections.cbmc as cbmc
import mc3s_pywrapper.sections.simbox as simbox
import mc3s_pywrapper.sections.mtype as mtype
import mc3s_pywrapper.sections.atom as atom
import mc3s_pywrapper.sections.bond as bond
import mc3s_pywrapper.sections.angle as angle
import mc3s_pywrapper.sections.dihedral as dihedral
import mc3s_pywrapper.sections.shared as shared
import mc3s_pywrapper.sections.analysis as analysis
import mc3s_pywrapper.sections.external_field as external_field
import mc3s_pywrapper.sections.swatch as swatch
import mc3s_pywrapper.sections.flucq as flucq
import mc3s_pywrapper.sections.gcmc as gcmc
import mc3s_pywrapper.sections.ee as ee
# Custom sections
import mc3s_pywrapper.sections.swap_table as swap_table
# Logging
#import mc3s_pywrapper.utilities.job_log

class Sim:

  def __init__(self,execPath,name="mcsim"):

    self.__name               = name
    self.__prod               = False
    self.__ncycles            = None
    self.__errorLog           = []
    self.__changeLog          = chl.changeLog()
    self.__changeLogFile      = "{}-changelog.txt".format(self.__name)
    self.__errorLogFile       = "{}-errorlog.txt".format(self.__name)
    self.__location           = "Sim"
    self.__jobLog             = {} # Will make this more full-featured later
#    self.__homeDirectory      = os.getcwd()
#    self.__scratchDirectory   = None
    self.__topmonFile         = None #"{}/topmon.inp".format(self.__homeDirectory)
    self.__fort4File          = None #"{}/fort.4".format(self.__homeDirectory)
    self.__boxes              = None
    self.__atoms              = None
    self.__bonds              = None
    self.__angles             = None
    self.__dihedrals          = None
    self.__mtypes             = None
    self.__code               = code.Code(execPath=execPath,changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__runtime            = runtime.Runtime(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__io                 = io.IO(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__checkpoint         = checkpoint.Checkpoint(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__system             = system.System(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__shared             = shared.Shared(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__analysis           = analysis.Analysis(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__volume             = volume.Volume(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__swap               = swap.Swap(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__cbmc               = cbmc.CBMC(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__simple             = simple.Simple(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__external_field     = external_field.External_field(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__swatch             = swatch.Swatch(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__flucq              = flucq.FlucQ(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__gcmc               = gcmc.GCMC(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__ee                 = ee.EE(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__swap_table         = None
    self.__swatch_table       = None

  @property
  def name(self):
    return self.__name

  @property
  def prod(self):
    return self.__prod

  @property
  def ncycles(self):
    return self.__ncycles

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

#  @property
#  def homeDirectory(self):
#    return self.__homeDirectory
#
#  @property
#  def scratchDirectory(self):
#    return self.__scratchDirectory

  @property
  def topmonFile(self):
    return self.__topmonFile

  @property
  def fort4File(self):
    return self.__fort4File

  @property
  def code(self):
    return self.__code

  @property
  def runtime(self):
    return self.__runtime

  @property
  def io(self):
    return self.__io

  @property
  def checkpoint(self):
    return self.__checkpoint

  @property
  def system(self):
    return self.__system

  @property
  def shared(self):
    return self.__shared

  @property
  def analysis(self):
    return self.__analysis

  @property
  def volume(self):
    return self.__volume

  @property
  def swap(self):
    return self.__swap

  @property
  def cbmc(self):
    return self.__cbmc

  @property
  def simple(self):
    return self.__simple
  
  @property
  def external_field(self):
    return self.__external_field
  
  @property
  def swatch(self):
    return self.__swatch

  @property
  def flucq(self):
    return self.__flucq
  
  @property
  def gcmc(self):
    return self.__gcmc

  @property
  def ee(self):
    return self.__ee

  @property
  def boxes(self):
    return self.__boxes

  @property
  def atoms(self):
    return self.__atoms

  @property
  def bonds(self):
    return self.__bonds

  @property
  def angles(self):
    return self.__angles

  @property
  def dihedrals(self):
    return self.__dihedrals

  @property
  def mtypes(self):
    return self.__mtypes

  @property
  def swap_table(self):
    return self.__swap_table

  # For more advanced sections (i.e. not the namelists), I need to have these constructors.
  # This is because they build my custom objectArray to allow full access to getters/setters
  # of individual elements. This requires the user to specify how large each array is.
  def init_boxes(self,nbox):
    boxes = []
    for i in range(1,nbox+1):
      boxes.append(simbox.SimBox(number=i,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                 location=self.__location))
    self.__boxes = oba.objectArray.listToOBA(boxes,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                             location=self.__location)

  def init_mtypes(self,nmolty):
    mtypes = []
    for i in range(nmolty):
      mtypes.append(mtype.MType(number=i+1,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                location=self.__location))
    self.__mtypes = oba.objectArray.listToOBA(mtypes,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                             location=self.__location)

  def init_atoms(self,natomty):
    atoms = []
    for i in range(natomty):
      atoms.append(atom.Atom(number=i+1,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                location=self.__location))
    self.__atoms = oba.objectArray.listToOBA(atoms,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                                location=self.__location)

  def init_bonds(self,nbonds):
    bonds = []
    for i in range(nbonds):
      bonds.append(bond.Bond(number=i+1,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                location=self.__location))
    self.__bonds = oba.objectArray.listToOBA(bonds,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                                location=self.__location)

  def init_angles(self,nangles):
    angles = []
    for i in range(nangles):
      angles.append(angle.Angle(number=i+1,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                location=self.__location))
    self.__angles = oba.objectArray.listToOBA(angles,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                              location=self.__location)

  def init_dihedrals(self,ndihedrals):
    dihedrals = []
    for i in range(ndihedrals):
      dihedrals.append(dihedral.Dihedral(number=i+1,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                         location=self.__location))
    self.__dihedrals = oba.objectArray.listToOBA(dihedrals,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                                 location=self.__location)

#  def init_swap_table(self, nmolty, nswapb, probabilities=None, boxPairs=None):
#    '''
#        Instantiate the swap table found in SECTION MC_SWAP. Need to know the number of molecule types
#        and how many box pairs are specified for each molecule type.
#    '''
#
#    assert len(nswapb) == nmolty, "# of moltypes and length of nswapb don't match"
#    if probabilities:
#      assert len(probabilities) == nmolty, "# of moltypes and length of probabilities list don't match"
#
#    nswapb = oda.listToODA(
#      nswapb, errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location
#    )
#
#    # Setting the probability for a move between each box pair is optional at this stage. If the
#    # probabilities are unspecified (they must be specified in whole), then they are left as None.
#    if probabilities:
#      probs = []
#      # The probabilities are a list of probabilities between each box pair specified for each moltype.
#      # Hence, we must make one of the objectArrays for this.      
#      for plist in probabilities:
#        myODA = oda.oneDimArray.listToODA(
#          plist, errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location
#        )
#        probs.append(myODA)
#    else:
#      probs = None
#      #for i in range(nmolty):
#      #  myODA = oda.oneDimArray.listToODA(
#      #    [0.0]*nswapb[i], errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location
#      #  )
#      #  probs.append(myODA)
#
#    # Setting the list of box pairs is optional at this stage. If they are unspecified 
#    # (they must be specified in whole), then they are left as None.
#    if boxPairs:
#      pairs = []     
#      for plist in boxPairs:
#        myODA = oda.oneDimArray.listToODA(
#          [tuple(v) for v in plist], errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location
#        )
#        pairs.append(myODA)
#    else:
#      pairs = None
#    
#    self.__swap_table = swap_table.SwapTable(
#      nswapb=nswapb, pmswapb=probs, boxPairs=pairs, errorLog=self.__errorLog, changeLog=self.__changeLog,
#      location=self.__location
#    )

  def init_swap_table(self, nmolty):
    stables = []
    for i in range(nmolty):
      stables.append(
        swap_table.SwapTable(
          number=i+1,errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location
        )
      )
    self.__swap_table = oba.objectArray.listToOBA(
      stables,errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location
    )

  def write_topmon(self,topmonFile=None):
    if topmonFile is None:
      topmonFile = self.__topmonFile
    tw.write_topmon(self,topmonFile=topmonFile)

  def write_fort4(self,fort4File=None):
    if fort4File is None:
      fort4File = self.__fort4File
    fw.write_fort4(self,fort4File=fort4File)

  def write_errorLog(self,fn=None):
    # No argument or explicit None prints to screen
    if fn is None:
      for error in self.__errorLog:
        print(error)

  def write_changeLog(self,keys=None,mask=None,outFile=None,overwrite=True,printToScreen=False):

    if keys is not None and mask is None:
      chlog = self.__changeLog.returnAbbreviated(keys)
    elif mask is not None:
      chlog = self.__changeLog.returnMask(mask)
      if keys is not None:
        chlog = chl.returnAbbreviated(keys)
    else:
      chlog = self.__changeLog.copy()

    # No argument or explicit None prints to screen
    if outFile is None:
      outFile = self.__changeLogFile

    log = "Begin entry: {}\n\n".format(dt.datetimePrettify(datetime.datetime.now()))

    for ch in chlog.data:

      dictKeys = ch.keys()

      if "Location" in dictKeys:
        log += "  {:<20s}: {:<40s}\n".format("Location",ch["Location"])
      if "Variable" in dictKeys:
        log += "  {:<20s}: {:<40s}\n".format("Variable",ch["Variable"])
      if "Index" in dictKeys:
        log += "  {:<20s}: {:<40s}\n".format("Index",str(ch["Index"]))
      if "New" in dictKeys:
        log += "  {:<20s}: {:<40s}\n".format("New",str(ch["New"]))
      if "Previous" in dictKeys:
        log += "  {:<20s}: {:<40s}\n".format("Previous",str(ch["Previous"]))
      if "Success" in dictKeys:
        log += "  {:<20s}: {:<40s}\n".format("Success",str(ch["Success"]))
      if "Date" in dictKeys:
        log += "  {:<20s}: {:<40s}\n".format("Date",dt.datetimePrettify(ch["Date"]))
      if "ErrorMessage" in dictKeys:
        log += "  {:<20s}: {:<40s}\n".format("ErrorMessage",str(ch["ErrorMessage"]))

      log += "\n\n"

    if printToScreen:
      print(log)

    else:
      if overwrite:
        wtype = "w"
      else:
        wtype = "a+"
      with open(outFile,wtype) as f:
        f.write(log)

  def run_mc3s(self, workdir=None):
    """
        Run the MCCCS-MN executable
    """

    if workdir:
      os.chdir(workdir)

    start = time.ctime(time.time())
    args = [self.exec_path]

    if self.runtime.nProc:
      args += ["-n", self.runtime.nProc]
    if self.runtime.nThreadsPerProc:
      args += ["--threads", self.runtime.nThreadsPerProc]
    if self.topmonFile:
      args += ["--input", self.topmonFile]

    rc = subprocess.check_call(args)

    end = time.ctime(time.time())

    return start, end, os.getcwd(), rc == 0, None

  def logJob(
    self, start, end, direc, success, msg, name, copy=False
  ):
  
    self.__jobLog[name] = {
      "start_time": start,
      "end_time": end,
      "directory": direc,
      "success": success,
      "slurm_message": msg,
    }
    
    # copy functionality is so that we can reuse project
    # workdirs without designating a "stage" (i.e. "melt" or "cool")
    # in the project schema
    if copy:
      for fn in os.path.listdir(direc):
        shutil.copyfile(
          os.path.join(direc, fn), os.path.join(direc, f"{name}.{fn}")
        )
        

  @classmethod
  def from_inputs(cls, topmon, execPath, fort4=None, name="mcsim"):
    """
        Construct a Sim object from input files (topmon.inp, optionally fort.4). If no fort.4 file
        path is passed, it will be assumed that the fort.4 file can be inferred from the 'io' section
        of the topmon file.

        Input:
            topmon [str, os.path.abspath]: Path to topmon.inp file
            execPath [str, os.path.abspath]: Path to MCCCS-MN executable
            fort4 [Optional[str, os.path.abspath]]: Path to fort.4 file (optional, may be inferred from
                topmon.inp io section)
            name [Optional[str]]: Optional name for the `name` section of the Sim object
        Output:
            A Sim() instance with inputs properly sourced from the arguments/input files.
    """

    mc_sim = cls(execPath, name=name)
    mc_sim = read_topmon(topmon, mc_sim=mc_sim)
    if fort4:
      mc_sim = read_fort4(fort4, mc_sim=mc_sim)
    else:
      assert mc_sim.io.file_input, "Didn't pass file_input and couldn't be inferred from topmon"
      mc_sim = read_fort4(mc_sim.io.file_input, mc_sim=mc_sim)