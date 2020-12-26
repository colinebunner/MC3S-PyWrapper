import datetime
from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda

class Atom:

  def __init__(self,aType=None,vdWParams=None,charge=None,mass=None,intID=None,chemID=None,chName=None,errorLog=[],
               changeLog=[],location="",number=None):

    self.__intID     = intID
    self.__aType     = aType
    self.__vdWParams = vdWParams
    self.__charge    = charge
    self.__mass      = mass
    self.__chemID    = chemID
    self.__chName    = chName
    self.__number    = number
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/Atom-{}".format(location,number)

  @property
  def intID(self):
    return self.__intID

  @property
  def aType(self):
    return self.__aType

  @property
  def vdWParams(self):
    return self.__vdWParams

  @property
  def charge(self):
    return self.__charge

  @property
  def mass(self):
    return self.__mass

  @property
  def chemID(self):
    return self.__chemID

  @property
  def chName(self):
    return self.__chName

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

  @vdWParams.setter
  def vdWParams(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or ti.is_probability):
          errorMessage = ("To properly set vdWParams you have a few options. You can pass it as a "
                          " python list (e.g. mySim.volume.vdWParams = [3.5,160.0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Not that single values can be passed as a float/int, but they "
                          " must be less than or equal to 1.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'vdWParams','Success':False,'Previous':repr(self.__vdWParams),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'vdWParams',
                                  'ErrorMessage':errorMessage})
      else:
        if not isinstance(val,list):
          val = [val]
        length = len(val)
        myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="vdWParams")
        self.__vdWParams = myODA
        for i in range(length):
          self.__vdWParams[i+1] = val[i]

    else:
      length = val.length
      myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                        location=self.__location,var="vdWParams")
      self.__vdWParams = myODA
      for i in range(length):
        self.__vdWParams[i+1] = val[i]

  @charge.setter
  def charge(self,val):
    if ti.is_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'charge','Success':True,'Previous':self.__charge,'New':val,
                               'ErrorMessage':None})
      self.__charge = val
    else:
      errorMessage = "charge must be a number."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'charge','Success':False,'Previous':self.__charge,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'charge','ErrorMessage':errorMessage})

  @mass.setter
  def mass(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'mass','Success':True,'Previous':self.__mass,'New':val,
                               'ErrorMessage':None})
      self.__mass = val
    else:
      errorMessage = "mass must be a positive number."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'mass','Success':False,'Previous':self.__mass,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'mass','ErrorMessage':errorMessage})

  @chemID.setter
  def chemID(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                             'Variable':'chemID','Success':True,'Previous':self.__chemID,'New':val,
                             'ErrorMessage':None})
    self.__chemID = val

  @chName.setter
  def chName(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                             'Variable':'chName','Success':True,'Previous':self.__chName,'New':val,
                             'ErrorMessage':None})
    self.__chName = val
