import datetime
from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda

class Bond:

  def __init__(
    self,intID=None,bType=None,bondParams=None,minimumRegrow=None,
    maximumRegrow=None,errorLog=[],changeLog=[],location="",number=None
  ):

    self.__intID         = intID
    self.__bType         = bType
    self.__bondParams    = bondParams
    self.__minimumRegrow = minimumRegrow
    self.__maximumRegrow = maximumRegrow
    self.__number        = number
    self.__errorLog      = errorLog
    self.__changeLog     = changeLog
    self.__location      = "{}/Bond-{}".format(location,number)

  @property
  def intID(self):
    return self.__intID

  @property
  def bType(self):
    return self.__bType

  @property
  def bondParams(self):
    return self.__bondParams

  @property
  def minimumRegrow(self):
    return self.__minimumRegrow
  
  @property
  def maximumRegrow(self):
    return self.__maximumRegrow

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

  @bType.setter
  def bType(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'bType','Success':True,'Previous':self.__bType,'New':val,
                                'ErrorMessage':None})
      self.__bType = val
    else:
      errorMessage = "bType must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'bType','Success':False,'Previous':self.__bType,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'bType','ErrorMessage':errorMessage})

  @bondParams.setter
  def bondParams(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or ti.is_probability):
          errorMessage = ("To properly set bondParams you have a few options. You can pass it as a "
                          " python list (e.g. mySim.bonds[1].bondParams = [1.55, 0.0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Not that single values can be passed as a float/int, but they "
                          " must be less than or equal to 1.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'bondParams','Success':False,'Previous':repr(self.__bondParams),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'bondParams',
                                  'ErrorMessage':errorMessage})
      else:
        if not isinstance(val,list):
          val = [val]
        length = len(val)
        myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="bondParams")
        self.__bondParams = myODA
        for i in range(length):
          self.__bondParams[i+1] = val[i]

    else:
      length = val.length
      myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                        location=self.__location,var="bondParams")
      self.__bondParams = myODA
      for i in range(length):
        self.__bondParams[i+1] = val[i]

  @minimumRegrow.setter
  def minimumRegrow(self, val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'minimumRegrow','Success':True,'Previous':self.__minimumRegrow,'New':val,
                                'ErrorMessage':None})
      self.__minimumRegrow = val
    else:
      errorMessage = "minimumRegrow must be a positive number."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'minimumRegrow','Success':False,'Previous':self.__minimumRegrow,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'minimumRegrow','ErrorMessage':errorMessage})

  @maximumRegrow.setter
  def maximumRegrow(self, val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'maximumRegrow','Success':True,'Previous':self.__maximumRegrow,'New':val,
                                'ErrorMessage':None})
      self.__maximumRegrow = val
    else:
      errorMessage = "maximumRegrow must be a positive number."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'maximumRegrow','Success':False,'Previous':self.__maximumRegrow,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'maximumRegrow','ErrorMessage':errorMessage})
