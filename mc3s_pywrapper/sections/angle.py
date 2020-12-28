import datetime
from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda

class Angle:

  def __init__(self,intID=None,aType=None,angleParams=None,errorLog=[],
               changeLog=[],location="",number=None):

    self.__intID       = intID
    self.__aType       = aType
    self.__angleParams = angleParams
    self.__number      = number
    self.__errorLog    = errorLog
    self.__changeLog   = changeLog
    self.__location    = "{}/Angle-{}".format(location,number)

  @property
  def intID(self):
    return self.__intID

  @property
  def aType(self):
    return self.__aType

  @property
  def angleParams(self):
    return self.__angleParams

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

  @angleParams.setter
  def angleParams(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or ti.is_probability):
          errorMessage = ("To properly set angleParams you have a few options. You can pass it as a "
                          " python list (e.g. mySim.angles[1].angleParams = [1.55, 0.0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Not that single values can be passed as a float/int, but they "
                          " must be less than or equal to 1.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'angleParams','Success':False,'Previous':repr(self.__angleParams),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'angleParams',
                                  'ErrorMessage':errorMessage})
      else:
        if not isinstance(val,list):
          val = [val]
        length = len(val)
        myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="angleParams")
        self.__angleParams = myODA
        for i in range(length):
          self.__angleParams[i+1] = val[i]

    else:
      length = val.length
      myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                        location=self.__location,var="angleParams")
      self.__angleParams = myODA
      for i in range(length):
        self.__angleParams[i+1] = val[i]
