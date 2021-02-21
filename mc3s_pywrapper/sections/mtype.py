import datetime
from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import objectArray   as oba
from mc3s_pywrapper.sections  import bead

class MType:

  def __init__(self,nunit=None,nugrow=None,num_growpoints=None,ncarbon=None,maxcbmc=None,maxgrow=None,iring=None,
               lelect=None,lring=None,lrigid=None,lbranch=None,lsetup=None,lq14scale=None,qscale=None,
               iurot=None,isolute=None,beads=None,growpoints=None,errorLog=[],changeLog=[],location="",number=None):

    self.__nunit     = nunit
    self.__nugrow    = nugrow
    self.__num_growpoints = num_growpoints
    self.__ncarbon   = ncarbon
    self.__maxcbmc   = maxcbmc
    self.__maxgrow   = maxgrow
    self.__iring     = iring
    self.__lelect    = lelect
    self.__lring     = lring
    self.__lrigid    = lrigid
    self.__lbranch   = lbranch
    self.__lsetup    = lsetup
    self.__lq14scale = lq14scale
    self.__qscale    = qscale
    self.__iurot     = iurot
    self.__isolute   = isolute
    self.__beads     = beads
    self.__growpoints = growpoints
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/mtype-{}".format(location,number)

  def init_beads(self,nbeads=None):
    if nbeads is None:
      nbeads = self.__nunit
    beads = []
    for i in range(nbeads):
      beads.append(bead.Bead(errorLog=self.__errorLog,changeLog=self.__changeLog,
                             location=self.__location,unit=i+1))
    self.__beads = oba.objectArray.listToOBA(beads,errorLog=[],changeLog=[],location="",var="")

  @property
  def nunit(self):
    return self.__nunit

  @property
  def nugrow(self):
    return self.__nugrow

  @property
  def num_growpoints(self):
    return self.__num_growpoints


  @property
  def ncarbon(self):
    return self.__ncarbon

  @property
  def maxcbmc(self):
    return self.__maxcbmc

  @property
  def maxgrow(self):
    return self.__maxgrow

  @property
  def iring(self):
    return self.__iring

  @property
  def lelect(self):
    return self.__lelect

  @property
  def lring(self):
    return self.__lring

  @property
  def lrigid(self):
    return self.__lrigid

  @property
  def lbranch(self):
    return self.__lbranch

  @property
  def lsetup(self):
    return self.__lsetup

  @property
  def lq14scale(self):
    return self.__lq14scale

  @property
  def qscale(self):
    return self.__qscale

  @property
  def iurot(self):
    return self.__iurot

  @property
  def isolute(self):
    return self.__isolute

  @property
  def beads(self):
    return self.__beads

  @property
  def growpoints(self):
    return self.__growpoints

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @nunit.setter
  def nunit(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nunit','Success':True,'Previous':self.__nunit,'New':val,
                               'ErrorMessage':None})

      self.__nunit = val
    else:
      errorMessage = "nunit must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nunit','Success':False,'Previous':self.__nunit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nunit','ErrorMessage':errorMessage})

  @nugrow.setter
  def nugrow(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nugrow','Success':True,'Previous':self.__nugrow,'New':val,
                               'ErrorMessage':None})

      self.__nugrow = val
    else:
      errorMessage = "nugrow must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nugrow','Success':False,'Previous':self.__nugrow,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nugrow','ErrorMessage':errorMessage})

  @num_growpoints.setter
  def num_growpoints(self,val):
    if ti.is_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'num_growpoints','Success':True,'Previous':self.__num_growpoints,'New':val,
                               'ErrorMessage':None})

      self.__num_growpoints = val
    else:
      errorMessage = "num_growpoints must be an integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'num_growpoints','Success':False,'Previous':self.__num_growpoints,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'num_growpoints','ErrorMessage':errorMessage})

  @ncarbon.setter
  def ncarbon(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ncarbon','Success':True,'Previous':self.__ncarbon,'New':val,
                               'ErrorMessage':None})

      self.__ncarbon = val
    else:
      errorMessage = "ncarbon must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ncarbon','Success':False,'Previous':self.__ncarbon,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ncarbon','ErrorMessage':errorMessage})

  @maxcbmc.setter
  def maxcbmc(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'maxcbmc','Success':True,'Previous':self.__maxcbmc,'New':val,
                               'ErrorMessage':None})

      self.__maxcbmc = val
    else:
      errorMessage = "maxcbmc must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'maxcbmc','Success':False,'Previous':self.__maxcbmc,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'maxcbmc','ErrorMessage':errorMessage})

  @maxgrow.setter
  def maxgrow(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'maxgrow','Success':True,'Previous':self.__maxgrow,'New':val,
                               'ErrorMessage':None})

      self.__maxgrow = val
    else:
      errorMessage = "maxgrow must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'maxgrow','Success':False,'Previous':self.__maxgrow,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'maxgrow','ErrorMessage':errorMessage})

  @iring.setter
  def iring(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iring','Success':True,'Previous':self.__iring,'New':val,
                               'ErrorMessage':None})

      self.__iring = val
    else:
      errorMessage = "iring must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iring','Success':False,'Previous':self.__iring,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iring','ErrorMessage':errorMessage})

  @lelect.setter
  def lelect(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lelect','Success':True,'Previous':self.__lelect,'New':val,
                               'ErrorMessage':None})

      self.__lelect = val
    else:
      errorMessage = "lelect must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lelect','Success':False,'Previous':self.__lelect,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lelect','ErrorMessage':errorMessage})

  @lring.setter
  def lring(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lring','Success':True,'Previous':self.__lring,'New':val,
                               'ErrorMessage':None})

      self.__lring = val
    else:
      errorMessage = "lring must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lring','Success':False,'Previous':self.__lring,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lring','ErrorMessage':errorMessage})

  @lrigid.setter
  def lrigid(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lrigid','Success':True,'Previous':self.__lrigid,'New':val,
                               'ErrorMessage':None})

      self.__lrigid = val
    else:
      errorMessage = "lrigid must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lrigid','Success':False,'Previous':self.__lrigid,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lrigid','ErrorMessage':errorMessage})

  @lbranch.setter
  def lbranch(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lbranch','Success':True,'Previous':self.__lbranch,'New':val,
                               'ErrorMessage':None})

      self.__lbranch = val
    else:
      errorMessage = "lbranch must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lbranch','Success':False,'Previous':self.__lbranch,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lbranch','ErrorMessage':errorMessage})

  @lsetup.setter
  def lsetup(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lsetup','Success':True,'Previous':self.__lsetup,'New':val,
                               'ErrorMessage':None})

      self.__lsetup = val
    else:
      errorMessage = "lsetup must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lsetup','Success':False,'Previous':self.__lsetup,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lsetup','ErrorMessage':errorMessage})

  @lq14scale.setter
  def lq14scale(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lq14scale','Success':True,'Previous':self.__lq14scale,
                               'New':val,'ErrorMessage':None})

      self.__lq14scale = val
    else:
      errorMessage = "lq14scale must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lq14scale','Success':False,'Previous':self.__lq14scale,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lq14scale','ErrorMessage':errorMessage})

  @qscale.setter
  def qscale(self,val):
    if ti.is_positive_number(val) and val < 1.0:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'qscale','Success':True,'Previous':self.__qscale,
                               'New':val,'ErrorMessage':None})

      self.__qscale = val
    else:
      errorMessage = "qscale must be a positive number that is less than or equal to 1."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'qscale','Success':False,'Previous':self.__qscale,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'qscale','ErrorMessage':errorMessage})

  @iurot.setter
  def iurot(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iurot','Success':True,'Previous':self.__iurot,'New':val,
                               'ErrorMessage':None})

      self.__iurot = val
    else:
      errorMessage = "iurot must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iurot','Success':False,'Previous':self.__iurot,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iurot','ErrorMessage':errorMessage})

  @isolute.setter
  def isolute(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'isolute','Success':True,'Previous':self.__isolute,'New':val,
                               'ErrorMessage':None})

      self.__isolute = val
    else:
      errorMessage = "isolute must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'isolute','Success':False,'Previous':self.__isolute,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'isolute','ErrorMessage':errorMessage})

  @beads.setter
  def beads(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        if not isinstance(val,bead.Bead):
          errorMessage = (" There are two easy ways to set beads:\n 1) Read a molecule type from file\n"
                          " 2) Call init_beads(nbeads), which will create nbeads bead objects"
                          " whose information can be updated.\n You can also make your own bead objects,"
                          " (myBead1 = bead.Bead()), concatenate as a list, and use the oneDimArray "
                          " listToODA method; however, this is not a preferred way as you would have to "
                          " pass the right errorLog, changeLog, location, and variable variables by "
                          " reference to properly log changes.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'beads','Success':False,'Previous':repr(self.__beads),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'beads',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="beads")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'beads','Success':True,'Previous':repr(self.__beads),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__beads = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'beads','Success':True,'Previous':repr(self.__beads),
                                 'New':repr(val),'ErrorMessage':None})
      self.__beads = val

  @growpoints.setter
  def growpoints(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        print(type(val))
        if not isinstance(val,int):
          errorMessage = (" Error setting growpoints")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'growpoints','Success':False,'Previous':repr(self.__growpoints),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'growpoints',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="growpoints")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'growpoints','Success':True,'Previous':repr(self.__growpoints),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__growpoints = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'growpoints','Success':True,'Previous':repr(self.__growpoints),
                                 'New':repr(val),'ErrorMessage':None})
      self.__growpoints = val
