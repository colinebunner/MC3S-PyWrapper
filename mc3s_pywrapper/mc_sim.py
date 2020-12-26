# Python standard modules
import os
import datetime
import random
# Our module files
from mc3s_pywrapper.utilities import oneDimArray as oda
from mc3s_pywrapper.utilities import objectArray as oba
from mc3s_pywrapper.utilities import dateTools   as dt
from mc3s_pywrapper.utilities import changeLog   as chl
from mc3s_pywrapper.writers   import write_topmon as tw
from mc3s_pywrapper.writers   import write_fort4 as fw
import mc3s_pywrapper.sections.code as code
import mc3s_pywrapper.sections.runtime as runtime
import mc3s_pywrapper.sections.io as io
import mc3s_pywrapper.sections.checkpoint as checkpoint
import mc3s_pywrapper.sections.system as system
import mc3s_pywrapper.sections.volume as volume
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
    self.__homeDirectory      = os.getcwd()
    self.__scratchDirectory   = None
    self.__topmonFile         = "{}/topmon.inp".format(self.__homeDirectory)
    self.__fort4File          = "{}/fort.4".format(self.__homeDirectory)
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

  @property
  def homeDirectory(self):
    return self.__homeDirectory

  @property
  def scratchDirectory(self):
    return self.__scratchDirectory

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
