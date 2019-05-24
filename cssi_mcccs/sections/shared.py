import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class Shared:

  def __init__(self,seed=None,nbox=None,nmolty=None,nstep=None,lstop=None,iratio=None,rmin=None,
               softcut=None,linit=None,lreadq=None,nchain=None,errorLog=[],changeLog=[],location=""):
    
    self.__seed = seed
    self.__nbox = nbox
    self.__nmolty = nmolty
    self.__nstep  = nstep
    self.__lstop  = lstop
    self.__iratio = iratio
    self.__rmin   = rmin
    self.__softcut = softcut
    self.__linit   = linit
    self.__lreadq  = lreadq
    self.__nchain  = nchain
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/shared".format(location)

  @property
  def seed(self):
    return self.__seed

  @property
  def nbox(self):
    return self.__nbox

  @property
  def nmolty(self):
    return self.__nmolty
 
  @property
  def nstep(self):
    return self.__nmolty

  @property
  def lstop(self):
    return self.__lstop

  @property
  def iratio(self):
    return self.__iratio

  @property
  def rmin(self):
    return self.__rmin

  @property
  def softcut(self):
    return self.__softcut

  @property
  def linit(self):
    return self.__linit

  @property
  def lreadq(self):
    return self.__lreadq

  @property
  def nchain(self):
    return self.__nchain

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @seed.setter
  def seed(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'seed','Success':True,'Previous':self.__seed,'New':val,
                               'ErrorMessage':None})

      self.__seed = val
    else:
      errorMessage = "seed must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'seed','Success':False,'Previous':self.__seed,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'seed','ErrorMessage':errorMessage})

  @nbox.setter
  def nbox(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nbox','Success':True,'Previous':self.__nbox,'New':val,
                               'ErrorMessage':None})

      self.__nbox = val
    else:
      errorMessage = "nbox must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nbox','Success':False,'Previous':self.__nbox,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nbox','ErrorMessage':errorMessage})

  @nmolty.setter
  def nmolty(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nmolty','Success':True,'Previous':self.__nmolty,'New':val,
                               'ErrorMessage':None})

      self.__nmolty = val
    else:
      errorMessage = "nmolty must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nmolty','Success':False,'Previous':self.__nmolty,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nmolty','ErrorMessage':errorMessage})

  @nstep.setter
  def nstep(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nstep','Success':True,'Previous':self.__nstep,'New':val,
                               'ErrorMessage':None})

      self.__nstep = val
    else:
      errorMessage = "nstep must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nstep','Success':False,'Previous':self.__nstep,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nstep','ErrorMessage':errorMessage})

  @lstop.setter
  def lstop(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lstop','Success':True,'Previous':self.__lstop,'New':val,
                               'ErrorMessage':None})

      self.__lstop = val
    else:
      errorMessage = "lstop must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lstop','Success':False,'Previous':self.__lstop,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lstop','ErrorMessage':errorMessage})

  @iratio.setter
  def iratio(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iratio','Success':True,'Previous':self.__iratio,'New':val,
                               'ErrorMessage':None})

      self.__iratio = val
    else:
      errorMessage = "iratio must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iratio','Success':False,'Previous':self.__iratio,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iratio','ErrorMessage':errorMessage})

  @rmin.setter
  def rmin(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'rmin','Success':True,'Previous':self.__rmin,'New':val,
                               'ErrorMessage':None})

      self.__rmin = val
    else:
      errorMessage = "rmin must be a positive number."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'rmin','Success':False,'Previous':self.__rmin,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'rmin','ErrorMessage':errorMessage})

  @softcut.setter
  def softcut(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'softcut','Success':True,'Previous':self.__softcut,'New':val,
                               'ErrorMessage':None})

      self.__softcut = val
    else:
      errorMessage = "softcut must be a positive number."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'softcut','Success':False,'Previous':self.__softcut,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'softcut','ErrorMessage':errorMessage})

  @linit.setter
  def linit(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'linit','Success':True,'Previous':self.__linit,'New':val,
                               'ErrorMessage':None})

      self.__linit = val
    else:
      errorMessage = "linit must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'linit','Success':False,'Previous':self.__linit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'linit','ErrorMessage':errorMessage})

  @lreadq.setter
  def lreadq(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lreadq','Success':True,'Previous':self.__lreadq,'New':val,
                               'ErrorMessage':None})

      self.__lreadq = val
    else:
      errorMessage = "lreadq must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lreadq','Success':False,'Previous':self.__lreadq,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lreadq','ErrorMessage':errorMessage})

  @nchain.setter
  def nchain(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nchain','Success':True,'Previous':self.__nchain,'New':val,
                               'ErrorMessage':None})

      self.__nchain = val
    else:
      errorMessage = "nchain must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nchain','Success':False,'Previous':self.__nchain,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nchain','ErrorMessage':errorMessage})
