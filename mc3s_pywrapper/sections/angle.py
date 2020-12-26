import datetime
from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda

class Angle:

  def __init__(self,intID=None,aType=None,brben=None,brbenk=None,errorLog=[],
               changeLog=[],location="",number=None):

    self.__intID     = intID
    self.__aType     = aType
    self.__brben     = brben
    self.__brbenk    = brbenk
    self.__number    = number
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/Angle-{}".format(location,number)

  @property
  def intID(self):
    return self.__intID

  @property
  def aType(self):
    return self.__aType

  @property
  def brben(self):
    return self.__brben

  @property
  def brbenk(self):
    return self.__brbenk

  @property
  def number(self):
    return self.__number

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @intID.setter
  def intID(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'intID','Success':True,'Previous':self.__intID,'New':val,
                                'ErrorMessage':None})
      self.__intID = val
    else:
      errorMessage = "intID must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'intID','Success':False,'Previous':self.__intID,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'intID','ErrorMessage':errorMessage})

  @aType.setter
  def aType(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'aType','Success':True,'Previous':self.__aType,'New':val,
                                'ErrorMessage':None})
      self.__aType = val
    else:
      errorMessage = "aType must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'aType','Success':False,'Previous':self.__aType,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'aType','ErrorMessage':errorMessage})

  @brben.setter
  def brben(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'brben','Success':True,'Previous':self.__brben,'New':val,
                                'ErrorMessage':None})
      self.__brben = val
    else:
      errorMessage = "brben must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'brben','Success':False,'Previous':self.__brben,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'brben','ErrorMessage':errorMessage})

  @brbenk.setter
  def brbenk(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or ti.is_number):
          errorMessage = ("To properly set brbenk you have a few options. You can pass it as a "
                          " python list (e.g. mySim.angles[i].brbenk = [0.0e0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Not that single values can be passed as a float.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'brbenk','Success':False,'Previous':repr(self.__brbenk),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'brbenk',
                                  'ErrorMessage':errorMessage})
      else:
        if not isinstance(val,list):
          val = [val]
        length = len(val)
        myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                location=self.__location,var="brbenk")
        self.__brbenk = myODA
        for i in range(length):
          self.__brbenk[i+1] = val[i]

    else:
      length = val.length
      myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                        location=self.__location,var="brbenk")
      self.__brbenk = myODA
      for i in range(length):
        self.__brbenk[i+1] = val[i]
