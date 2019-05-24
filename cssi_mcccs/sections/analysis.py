import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class Analysis:

  def __init__(self,iprint=None,imv=None,iblock=None,iratp=None,idiele=None,iheatcapacity=None,
               ianalyze=None,nbin=None,lintra=None,lstretch=None,lgvst=None,lbend=None,lete=None,
               lrhoz=None,lucall=None,errorLog=[],changeLog=[],location=""):

    self.__iprint        = iprint
    self.__imv           = imv
    self.__iblock        = iblock
    self.__iratp         = iratp
    self.__idiele        = idiele
    self.__iheatcapacity = iheatcapacity
    self.__ianalyze      = ianalyze
    self.__nbin          = nbin
    self.__lintra        = lintra
    self.__lstretch      = lstretch
    self.__lgvst         = lgvst
    self.__lbend         = lbend
    self.__lete          = lete
    self.__lrhoz         = lrhoz
    self.__lucall        = lucall
    self.__errorLog      = errorLog
    self.__changeLog     = changeLog
    self.__location      = "{}/analysis".format(location)

  @property
  def iprint(self):
    return self.__iprint

  @property
  def imv(self):
    return self.__imv

  @property
  def iblock(self):
    return self.__iblock

  @property
  def iratp(self):
    return self.__iratp

  @property
  def idiele(self):
    return self.__idiele

  @property
  def iheatcapacity(self):
    return self.__iheatcapacity

  @property
  def ianalyze(self):
    return self.__ianalyze

  @property
  def nbin(self):
     return self.__nbin

  @property
  def lintra(self):
    return self.__lintra

  @property
  def lstretch(self):
    return self.__lstretch

  @property
  def lgvst(self):
    return self.__lgvst

  @property
  def lbend(self):
    return self.__lbend

  @property
  def lete(self):
    return self.__lete

  @property
  def lrhoz(self):
    return self.__lrhoz

  @property
  def lucall(self):
    return self.__lucall

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location()

  @iprint.setter
  def iprint(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iprint','Success':True,'Previous':self.__iprint,'New':val,
                               'ErrorMessage':None})

      self.__iprint = val
    else:
      errorMessage = "iprint must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iprint','Success':False,'Previous':self.__iprint,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iprint','ErrorMessage':errorMessage})

  @imv.setter
  def imv(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'imv','Success':True,'Previous':self.__imv,'New':val,
                               'ErrorMessage':None})

      self.__imv = val
    else:
      errorMessage = "imv must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'imv','Success':False,'Previous':self.__imv,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'imv','ErrorMessage':errorMessage})

  @iblock.setter
  def iblock(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iblock','Success':True,'Previous':self.__iblock,'New':val,
                               'ErrorMessage':None})

      self.__iblock = val
    else:
      errorMessage = "iblock must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iblock','Success':False,'Previous':self.__iblock,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iblock','ErrorMessage':errorMessage})

  @iratp.setter
  def iratp(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iratp','Success':True,'Previous':self.__iratp,'New':val,
                               'ErrorMessage':None})

      self.__iratp = val
    else:
      errorMessage = "iratp must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iratp','Success':False,'Previous':self.__iratp,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iratp','ErrorMessage':errorMessage})

  @idiele.setter
  def idiele(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'idiele','Success':True,'Previous':self.__idiele,'New':val,
                               'ErrorMessage':None})

      self.__idiele = val
    else:
      errorMessage = "idiele must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'idiele','Success':False,'Previous':self.__idiele,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'idiele','ErrorMessage':errorMessage})

  @iheatcapacity.setter
  def iheatcapacity(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iheatcapacity','Success':True,'Previous':self.__iheatcapacity,'New':val,
                               'ErrorMessage':None})

      self.__iheatcapacity = val
    else:
      errorMessage = "iheatcapacity must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iheatcapacity','Success':False,'Previous':self.__iheatcapacity,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iheatcapacity','ErrorMessage':errorMessage})

  @ianalyze.setter
  def ianalyze(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ianalyze','Success':True,'Previous':self.__ianalyze,'New':val,
                               'ErrorMessage':None})

      self.__ianalyze = val
    else:
      errorMessage = "ianalyze must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ianalyze','Success':False,'Previous':self.__ianalyze,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ianalyze','ErrorMessage':errorMessage})

  @nbin.setter
  def nbin(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nbin','Success':True,'Previous':self.__nbin,'New':val,
                               'ErrorMessage':None})

      self.__nbin = val
    else:
      errorMessage = "nbin must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nbin','Success':False,'Previous':self.__nbin,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nbin','ErrorMessage':errorMessage})

  @lintra.setter
  def lintra(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lintra','Success':True,'Previous':self.__lintra,'New':val,
                               'ErrorMessage':None})

      self.__lintra = val
    else:
      errorMessage = "lintra must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lintra','Success':False,'Previous':self.__lintra,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lintra','ErrorMessage':errorMessage})

  @lstretch.setter
  def lstretch(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lstretch','Success':True,'Previous':self.__lstretch,'New':val,
                               'ErrorMessage':None})

      self.__lstretch = val
    else:
      errorMessage = "lstretch must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lstretch','Success':False,'Previous':self.__lstretch,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lstretch','ErrorMessage':errorMessage})

  @lgvst.setter
  def lgvst(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lgvst','Success':True,'Previous':self.__lgvst,'New':val,
                               'ErrorMessage':None})

      self.__lgvst = val
    else:
      errorMessage = "lgvst must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lgvst','Success':False,'Previous':self.__lgvst,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lgvst','ErrorMessage':errorMessage})

  @lbend.setter
  def lbend(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lbend','Success':True,'Previous':self.__lbend,'New':val,
                               'ErrorMessage':None})

      self.__lbend = val
    else:
      errorMessage = "lbend must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lbend','Success':False,'Previous':self.__lbend,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lbend','ErrorMessage':errorMessage})

  @lete.setter
  def lete(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lete','Success':True,'Previous':self.__lete,'New':val,
                               'ErrorMessage':None})

      self.__lete = val
    else:
      errorMessage = "lete must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lete','Success':False,'Previous':self.__lete,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lete','ErrorMessage':errorMessage})

  @lrhoz.setter
  def lrhoz(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lrhoz','Success':True,'Previous':self.__lrhoz,'New':val,
                               'ErrorMessage':None})

      self.__lrhoz = val
    else:
      errorMessage = "lrhoz must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lrhoz','Success':False,'Previous':self.__lrhoz,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lrhoz','ErrorMessage':errorMessage})

  @lucall.setter
  def lucall(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lucall','Success':True,'Previous':self.__lucall,'New':val,
                               'ErrorMessage':None})

      self.__lucall = val
    else:
      errorMessage = "lucall must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lucall','Success':False,'Previous':self.__lucall,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lucall','ErrorMessage':errorMessage})
