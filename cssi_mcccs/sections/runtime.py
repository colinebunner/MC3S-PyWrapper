import datetime
import cssi_mcccs.utilities.test_instance as ti

class Runtime:

  def __init__(self,nProc=1,nThreadsPerProc=1,changeLog=[],errorLog=[],location=""):

    self.__nProc           = nProc
    self.__nThreadsPerProc = nThreadsPerProc
    self.__changeLog       = changeLog
    self.__errorLog        = errorLog
    self.__location        = location

  @property
  def nProc(self):
    return self.__nProc

  @property
  def nThreadsPerProc(self):
    return self.__nThreadsPerProc

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def location(self):
    return self.__location

  @nProc.setter
  def nProc(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'nProc',
                               'Success':True,'Previous':self.__nProc,'New':val,'ErrorMessage':None})
      self.__nProc = val
    else:
      errorMessage = "nProc must be a positive integer."
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nProc','ErrorMessage':errorMessage})
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'nProc',
                               'Success':False,'Previous':self.__nProc,'New':val,
                               'ErrorMessage':errorMessage})

  @nThreadsPerProc.setter
  def nThreadsPerProc(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nThreadsPerProc','Success':True,
                               'Previous':self.__nThreadsPerProc,'New':val,'ErrorMessage':None})
      self.__nThreadPerProc = val
    else:
      errorMessage = "nThreadsPerProc must be a positive integer."
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nThreadsPerProc','ErrorMessage':errorMessage})
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nThreadsPerProc','Success':False,
                               'Previous':self.__nThreadsPerProc,'New':val,'ErrorMessage':errorMessage})

