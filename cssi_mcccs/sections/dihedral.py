import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class Dihedral:

  def __init__(self,intID=None,dType=None,brben=None,vtt=None,errorLog=[],
               changeLog=[],location="",number=None):

    self.__intID     = intID
    self.__dType     = dType
    self.__vtt       = vtt
    self.__number    = number
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/Angle-{}".format(location,number)

  @property
  def intID(self):
    return self.__intID

  @property
  def dType(self):
    return self.__dType

  @property
  def vtt(self):
    return self.__vtt

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

  @dType.setter
  def dType(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'dType','Success':True,'Previous':self.__dType,'New':val,
                                'ErrorMessage':None})
      self.__dType = val
    else:
      errorMessage = "dType must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'dType','Success':False,'Previous':self.__dType,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'dType','ErrorMessage':errorMessage})

    @vtt.setter
    def vtt(self,val):
      if not isinstance(val,oda.oneDimArray):
        if not (isinstance(val,list) or ti.is_number):
            errorMessage = ("To properly set vtt you have a few options. You can pass it as a "
                            " python list (e.g. mySim.dihedrals[i].vtt = [0.0e0,1.0e0,-12.3e0])."
                            " This will automatically convert to the special oneDimArray used by the code."
                            " You can also set it as a oneDimArray object yourself, but this is far more "
                            " tedious and you need to be careful that the errorLog, changeLog, location, "
                            " and variable flags are set properly, which involves passing the right "
                            " reference. Note that single values can be passed as a float.")
            self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                     'Variable':'vtt','Success':False,'Previous':repr(self.__vtt),
                                     'New':repr(val),'ErrorMessage':errorMessage})
            self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                    'Location':self.__location,'Variable':'vtt',
                                    'ErrorMessage':errorMessage})
        else:
          if not isinstance(val,list):
            val = [val]
          length = len(val)
          myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                            location=self.__location,var="vtt")
          self.__vtt = myODA
          for i in range(length):
            self.__vtt[i+1] = val[i]

      else:
        length = val.length
        myODA = oda.oneDimArray(length,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="vtt")
        self.__vtt = myODA
        for i in range(length):
          self.__vtt[i+1] = val[i]
