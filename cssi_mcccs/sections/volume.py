import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class Volume:

  def __init__(self,tavol=None,iratv=None,pmvlmt=None,pmvolb=None,box5=None,box6=None,pmvol=None,
               pmvolx=None,pmvoly=None,rmvolume=None,allow_cutoff_failure=None,errorLog=[],changeLog=[],
               location=""):

    self.__tavol                = tavol
    self.__iratv                = iratv
    self.__pmvlmt               = pmvlmt
    self.__pmvolb               = pmvolb
    self.__box5                 = box5
    self.__box6                 = box6
    self.__pmvol                = pmvol
    self.__pmvolx               = pmvolx
    self.__pmvoly               = pmvoly
    self.__rmvolume             = rmvolume
    self.__allow_cutoff_failure = allow_cutoff_failure
    self.__errorLog             = errorLog
    self.__changeLog            = changeLog
    self.__location             = "{}/Volume".format(location)

  @property
  def tavol(self):
    return self.__tavol

  @property
  def iratv(self):
    return self.__iratv

  @property
  def pmvlmt(self):
    return self.__pmvlmt

  @property
  def pmvolb(self):
    return self.__pmvolb

  @property
  def box5(self):
    return self.__box5

  @property
  def box6(self):
    return self.__box6

  @property
  def pmvol(self):
    return self.__pmvol

  @property
  def pmvolx(self):
    return self.__pmvolx

  @property
  def pmvoly(self):
    return self.__pmvoly

  @property
  def rmvolume(self):
    return self.__rmvolume

  @property
  def allow_cutoff_failure(self):
    return self.__allow_cutoff_failure

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @tavol.setter
  def tavol(self,val):
    if ti.is_probability(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'tavol','Success':True,'Previous':self.__tavol,'New':val,
                               'ErrorMessage':None})

      self.__tavol = val
    else:
      errorMessage = "tavol must be a number less than 1."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'tavol','Success':False,'Previous':self.__tavol,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'tavol','ErrorMessage':errorMessage})

  @iratv.setter
  def iratv(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iratv','Success':True,'Previous':self.__iratv,'New':val,
                               'ErrorMessage':None})
      self.__iratv = val
    else:
      errorMessage = "iratv must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iratv','Success':False,'Previous':self.__iratv,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iratv','ErrorMessage':errorMessage})

  @pmvlmt.setter
  def pmvlmt(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or ti.is_probability(val)):
          errorMessage = ("To properly set pmvlmt you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.volume.pmvlmt = [1.0,1.0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as a float/int, but they "
                          " must be less than or equal to 1.0.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'pmvlmt','Success':False,'Previous':repr(self.__pmvlmt),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'pmvlmt',
                                  'ErrorMessage':errorMessage})
      else:
        if not isinstance(val,list):
          val = [val]
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="pmvlmt")
        self.__pmvlmt = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pmvlmt','Success':True,'Previous':repr(self.__pmvlmt),
                               'New':repr(val),'ErrorMessage':None})
      self.__pmvlmt = val

  @pmvolb.setter
  def pmvolb(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or ti.is_probability):
        errorMessage = ("To properly set pmvolb you have a few options. You can always pass it as a "
                        " python list (e.g. mySim.volume.pmvolb = [1.0,1.0])."
                        " This will automatically convert to the special oneDimArray used by the code."
                        " You can also set it as a oneDimArray object yourself, but this is far more "
                        " tedious and you need to be careful that the errorLog, changeLog, location, "
                        " and variable flags are set properly, which involves passing the right "
                        " reference. Not that single values can be passed as a float/int, but they "
                        " must be less than or equal to 1.")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'pmvolb','Success':False,'Previous':repr(self.__pmvolb),
                                 'New':repr(val),'ErrorMessage':errorMessage})
        self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                'Location':self.__location,'Variable':'pmvolb',
                                'ErrorMessage':errorMessage})
      else:
        if not isinstance(val,list):
          val = [val]
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="pmvolb")
        self.__pmvolb = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pmvolb','Success':True,'Previous':repr(self.__pmvolb),
                               'New':repr(val),'ErrorMessage':None})
      self.__pmvolb = val

  @pmvol.setter
  def pmvol(self,val):
    if ti.is_probability(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pmvol','Success':True,'Previous':self.__pmvol,'New':val,
                               'ErrorMessage':None})
      self.__pmvol = val
    else:
      errorMessage = "pmvol must be a number less than 1."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pmvol','Success':False,'Previous':self.__pmvol,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'pmvol','ErrorMessage':errorMessage})
