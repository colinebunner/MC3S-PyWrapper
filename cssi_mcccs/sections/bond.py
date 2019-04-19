import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class Bond:

  def __init__(self,intID=None,bType=None,brvib=None,brvibk=None,errorLog=[],
               changeLog=[],location="",number=None):

    self.__intID     = intID
    self.__bType     = bType
    self.__brvib     = brvib
    self.__brvibk    = brvibk
    self.__number    = number
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/Bond-{}".format(location,number)

  @property
  def intID(self):
    return self.__intID

  @property
  def bType(self):
    return self.__bType

  @property
  def brvib(self):
    return self.__brvib

  @property
  def brvibk(self):
    return self.__brvibk

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

  @brvib.setter
  def brvib(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'brvib','Success':True,'Previous':self.__brvib,'New':val,
                                'ErrorMessage':None})
      self.__brvib = val
    else:
      errorMessage = "brvib must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'brvib','Success':False,'Previous':self.__brvib,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'brvib','ErrorMessage':errorMessage})

  @brvibk.setter
  def brvibk(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or ti.is_number):
          errorMessage = ("To properly set brvibk you have a few options. You can pass it as a "
                          " python list (e.g. mySim.bonds[i].brvibk = [0.0e0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Not that single values can be passed as a float.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'brvibk','Success':False,'Previous':repr(self.__brvibk),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'brvibk',
                                  'ErrorMessage':errorMessage})
      else:
        if not isinstance(val,list):
          val = [val]
        length = len(val)
        myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="brvibk")
        self.__brvibk = myODA
        for i in range(length):
          self.__brvibk[i+1] = val[i]

    else:
      length = val.length
      myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                              location=self.__location,var="brvibk")
      self.__brvibk = myODA
      for i in range(length):
        self.__brvibk[i+1] = val[i]
