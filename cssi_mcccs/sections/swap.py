import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class Swap:

  def __init__(self,pmswap=None,pmswmt=None,errorLog=[],changeLog=[],location=""):
  
    self.__pmswap    = pmswap
    self.__pmswmt    = pmswmt
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/Swap".format(location)

  @property
  def pmswap(self):
    return self.__pmswap

  @property
  def pmswmt(self):
    return self.__pmswmt

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @pmswap.setter
  def pmswap(self,val):
    if ti.is_probability(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pmswap','Success':True,'Previous':self.__pmswap,'New':val,
                               'ErrorMessage':None})

      self.__pmswap = val
    else:
      errorMessage = "pmswap must be a number less than 1."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pmswap','Success':False,'Previous':self.__pmswap,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'pmswap','ErrorMessage':errorMessage})

  @pmswmt.setter
  def pmswmt(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_probability(val):
          errorMessage = ("To properly set pmsmt you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.pmswmt = [1.0,1.0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as a float/int, but they "
                          " must be less than or equal to 1.0.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'pmswmt','Success':False,'Previous':repr(self.__pmswmt),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'pmswmt',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="pmswmt")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'pmswmt','Success':True,'Previous':repr(self.__pmswmt),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__pmswmt = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'pmswmt','Success':True,'Previous':repr(self.__pmswmt),
                                 'New':repr(val),'ErrorMessage':None})
      self.__pmswmt = val
