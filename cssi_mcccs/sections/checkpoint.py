import datetime

import cssi_mcccs.utilities.test_instance as ti

class Checkpoint:

  def __init__(self,allowCheckpoint=False,checkpoint_interval=None,checkpoint_copies=None,
               use_checkpoint=None,changeLog=[],errorLog=[],location=""):

    #allowCheckpoint controls whether or not the checkpoint file is ever written out
    self.__use_checkpoint      = use_checkpoint
    if allowCheckpoint:
      self.__checkpoint_interval = checkpoint_interval
      self.__checkpoint_copies   = checkpoint_copies
    else:
      # Write checkpoint every 8 days
      self.__checkpoint_interval = 691200.0E0
      self.__checkpoint_copies   = 1
    self.__location              = "{}/Checkpoint".format(location)

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

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def location(self):
    return self.__location

  @allowCheckpoint.setter
  def allowCheckpoint(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                           'Variable':'allowCheckpoint','Success':True,'Previous':self.__allowCheckpoint,
                           'New':val,'ErrorMessage':None})
      self.__allowCheckpoint = val
    else:
      errorMessage = ("allowCheckpoint must be a boolean. Overwrite rejected.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'allowCheckpoint','Success':False,
                               'Previous':self.__allowCheckpoint,'New':val,'ErrorMessage':None})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'allowCheckpoint','ErrorMessage':errorMessage})

  @checkpoint_interval.setter
  def checkpoint_interval(self,val):
    if utilties.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'checkpoint_interval','Success':True,
                               'Previous':self.__checkpoint_interval,'New':val,'ErrorMessage':None})
      self.__checkpoint_interval = float(val)
    else:
      errorMessage = "checkpoint_interval must be a number."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'checkpoint_interval','Success':False,
                               'Previous':self.__checkpoint_interval,'New':val,'ErrorMessage':None})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'checkpoint_interval','ErrorMessage':errorMessage})

  @checkpoint_copies.setter
  def checkpoint_copies(self,val):
    if ti.is_positive_integer:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'checkpoint_copies','Success':True,
                               'Previous':self.__checkpoint_copies,'New':val,'ErrorMessage':None})
      self.__checkpoint_copies = val
    else:
      errorMessage = "checkpoint_copies must be an integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'checkpoint_copies','Success':False,
                               'Previous':self.__checkpoint_copies,'New':val,'ErrorMessage':None})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'checkpoint_copies','ErrorMessage':errorMessage})
