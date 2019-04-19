# Python standard modules
import os
import datetime
import random
# Our module files
from cssi_mcccs.utilities import oneDimArray as oda
from cssi_mcccs.utilities import objectArray as oba
from cssi_mcccs.utilities import dateTools   as dt
from cssi_mcccs.utilities import changeLog   as chl
import cssi_mcccs.sections.code as code
import cssi_mcccs.sections.runtime as runtime
import cssi_mcccs.sections.io as io
import cssi_mcccs.sections.checkpoint as checkpoint
import cssi_mcccs.sections.system as system
import cssi_mcccs.sections.volume as volume
import cssi_mcccs.sections.swap as swap
import cssi_mcccs.sections.cbmc as cbmc
import cssi_mcccs.sections.simbox as simbox
import cssi_mcccs.sections.mtype as mtype
import cssi_mcccs.sections.atom as atom
import cssi_mcccs.sections.bond as bond
import cssi_mcccs.sections.angle as angle
import cssi_mcccs.sections.dihedral as dihedral

class Sim:

  def __init__(self,execPath):

    self.__prod               = False
    self.__ncycles            = None
    self.__errorLog           = []
    self.__changeLog          = chl.changeLog()
    self.__location           = "Sim"
    self.__homeDirectory      = os.getcwd()
    self.__scratchDirectory   = None
    self.__boxes              = None
    self.__atoms              = None
    self.__bonds              = None
    self.__angles             = None
    self.__dihedrals          = None
    self.__code               = code.Code(execPath=execPath,changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__runtime            = runtime.Runtime(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__io                 = io.IO(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__checkpoint         = checkpoint.Checkpoint(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__system             = system.System(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__volume             = volume.Volume(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__swap               = swap.Swap(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)
    self.__cbmc               = cbmc.CBMC(changeLog=self.__changeLog,errorLog=self.__errorLog,location=self.__location)


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

  def write_errorLog(self,fn=None):
    # No argument or explicit None prints to screen
    if fn is None:
      for error in self.__errorLog:
        print(error)

  def write_changeLog(self,fn=None):
     # No argument or explicit None prints to screen
    if fn is None:
      for change in self.__changeLog:
        print(change)
