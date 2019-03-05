# Python standard modules
import os
import datetime
import random
# Our module files
import cssi_mcccs.classes.code as code
import cssi_mcccs.classes.runtime as runtime
import cssi_mcccs.classes.io as io

class Sim:

  def __init__(self,execPath):

    self.__prod               = False
    self.__ncycles            = 0
    self.__errorLog           = []
    self.__changeLog          = []
    self.__homeDirectory      = os.getcwd()
    self.__scratchDirectory   = "/tmp/cssi-mcccs-{}".format(int(random.random()*123456789))
    self.__code               = code.Code(execPath=execPath,changeLog=self.__changeLog,errorLog=self.__errorLog)
    self.__runtime            = runtime.Runtime(changeLog=self.__changeLog,errorLog=self.__errorLog)
    self.__io                 = io.IO(changeLog=self.__changeLog,errorLog=self.__errorLog)

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
