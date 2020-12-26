import datetime
from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda

class SimBox:

  def __init__(self,boxlx=None,boxly=None,boxlz=None,rcut=None,kalp=None,rcutnn=None,
               numDimensionIsIsotropic=None,lsolid=None,lrect=None,lideal=None,ltwice=None,
               temperature=None,pressure=None,nchain_mt=None,inix=None,iniy=None,iniz=None,inirot=None,
               inimix=None,zshift=None,dshift=None,use_linkcell=None,rintramax=None,errorLog=[],
               changeLog=[],location="",number=None):

    self.__boxlx                   = boxlx
    self.__boxly                   = boxly
    self.__boxlz                   = boxlz
    self.__rcut                    = rcut
    self.__kalp                    = kalp
    self.__rcutnn                  = rcutnn
    self.__numDimensionIsIsotropic = numDimensionIsIsotropic
    self.__lsolid                  = lsolid
    self.__lrect                   = lrect
    self.__lideal                  = lideal
    self.__ltwice                  = ltwice
    self.__temperature             = temperature
    self.__pressure                = pressure
    self.__nchain_mt               = nchain_mt
    self.__inix                    = inix
    self.__iniy                    = iniy
    self.__iniz                    = iniz
    self.__inirot                  = inirot
    self.__inimix                  = inimix
    self.__zshift                  = zshift
    self.__dshift                  = dshift
    self.__use_linkcell            = use_linkcell
    self.__rintramax               = rintramax
    self.__number                  = number
    self.__errorLog                = errorLog
    self.__changeLog               = changeLog
    self.__location                = "{}/SimBox-{}".format(location,number)

  def set_boxlengths(self,val):
    if not (isinstance(val,list) or isinstance(val,tuple)):
      errorMessage = "Couldn't set boxlength array because a list or tuple wasn't provided"
    elif (isinstance(val,list) or isinstance(val,tuple)) and len(val) != 3:
      errorMessage = "Couldn't set boxlength array because {} values were passed, not 3".format(len(val))
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxlx','Success':True,'Previous':self.__boxlx,'New':val[0],
                               'ErrorMessage':None})
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxly','Success':True,'Previous':self.__boxly,'New':val[1],
                               'ErrorMessage':None})
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxlz','Success':True,'Previous':self.__boxlz,'New':val[2],
                               'ErrorMessage':None})
      self.__boxlx = val[0]
      self.__boxly = val[1]
      self.__boxlz = val[2]

  @property
  def boxlx(self):
    return self.__boxlx

  @property
  def boxly(self):
    return self.__boxly

  @property
  def boxlz(self):
    return self.__boxlz

  @property
  def rcut(self):
    return self.__rcut

  @property
  def kalp(self):
    return self.__kalp

  @property
  def rcutnn(self):
    return self.__rcutnn

  @property
  def numDimensionIsIsotropic(self):
    return self.__numDimensionIsIsotropic

  @property
  def lsolid(self):
    return self.__lsolid

  @property
  def lrect(self):
    return self.__lrect

  @property
  def lideal(self):
    return self.__lideal

  @property
  def ltwice(self):
    return self.__ltwice

  @property
  def temperature(self):
    return self.__temperature

  @property
  def pressure(self):
    return self.__pressure

  @property
  def nchain_mt(self):
    return self.__nchain_mt

  @property
  def inix(self):
    return self.__inix

  @property
  def iniy(self):
    return self.__iniy

  @property
  def iniz(self):
    return self.__iniz

  @property
  def inirot(self):
    return self.__inirot

  @property
  def inimix(self):
    return self.__inimix

  @property
  def zshift(self):
    return self.__zshift

  @property
  def dshift(self):
    return self.__dshift

  @property
  def use_linkcell(self):
    return self.__use_linkcell

  @property
  def rintramax(self):
    return self.__rintramax

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

  @boxlx.setter
  def boxlx(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxlx','Success':True,'Previous':self.__boxlx,'New':val,
                               'ErrorMessage':None})
      self.__boxlx = val
    else:
      errorMessage("x box length must be a positive number")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxlx','Success':False,'Previous':self.__boxlx,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'boxlx','ErrorMessage':errorMessage})

  @boxly.setter
  def boxly(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxly','Success':True,'Previous':self.__boxly,'New':val,
                               'ErrorMessage':None})
      self.__boxly = val
    else:
      errorMessage("y box length must be a positive number")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxly','Success':False,'Previous':self.__boxly,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'boxly','ErrorMessage':errorMessage})

  @boxlz.setter
  def boxlz(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxlz','Success':True,'Previous':self.__boxlz,'New':val,
                               'ErrorMessage':None})
      self.__boxlz = val
    else:
      errorMessage("z box length must be a positive number")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'boxlz','Success':False,'Previous':self.__boxlz,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'boxlz','ErrorMessage':errorMessage})

  @rcut.setter
  def rcut(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'rcut','Success':True,'Previous':self.__rcut,'New':val,
                               'ErrorMessage':None})
      self.__rcut = val
    else:
      errorMessage("rcut must be a positive number")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'rcut','Success':False,'Previous':self.__rcut,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'rcut','ErrorMessage':errorMessage})

  @kalp.setter
  def kalp(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'kalp','Success':True,'Previous':self.__kalp,'New':val,
                               'ErrorMessage':None})
      self.__kalp = val
    else:
      errorMessage("kalp must be a positive number")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'kalp','Success':False,'Previous':self.__kalp,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'kalp','ErrorMessage':errorMessage})

  @rcutnn.setter
  def rcutnn(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'rcutnn','Success':True,'Previous':self.__rcutnn,'New':val,
                               'ErrorMessage':None})
      self.__rcutnn = val
    else:
      errorMessage("rcutnn must be a positive number")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'rcutnn','Success':False,'Previous':self.__rcutnn,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'rcutnn','ErrorMessage':errorMessage})

  @numDimensionIsIsotropic.setter
  def numDimensionIsIsotropic(self,val):
    if val in [0,2,3]:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'numDimensionIsIsotropic','Success':True,
                               'Previous':self.__numDimensionIsIsotropic,'New':val,
                               'ErrorMessage':None})
      self.__numDimensionIsIsotropic = val
    else:
      errorMessage = ("Allowed values for number of isotropic dimensions is 0, 2, or 3. You for some "
                      "reason though {} made sense.".format(val))
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'numDimensionIsIsotropic','Success':False,
                               'Previous':self.__numDimensionIsIsotropic,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'numDimensionIsIsotropic','ErrorMessage':errorMessage})

  @lsolid.setter
  def lsolid(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lsolid','Success':True,'Previous':self.__lsolid,'New':val,
                               'ErrorMessage':None})
      self.__lsolid = val
    else:
      errorMessage = ("lsolid must be a boolean")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lsolid','Success':False,'Previous':self.__lsolid,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lsolid','ErrorMessage':errorMessage})

  @lrect.setter
  def lrect(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lrect','Success':True,'Previous':self.__lrect,'New':val,
                               'ErrorMessage':None})
      self.__lrect = val
    else:
      errorMessage = ("lrect must be a boolean")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lrect','Success':False,'Previous':self.__lrect,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lrect','ErrorMessage':errorMessage})

  @lideal.setter
  def lideal(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lideal','Success':True,'Previous':self.__lideal,'New':val,
                               'ErrorMessage':None})
      self.__lideal = val
    else:
      errorMessage = ("lideal must be a boolean")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lideal','Success':False,'Previous':self.__lideal,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lideal','ErrorMessage':errorMessage})

  @ltwice.setter
  def ltwice(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ltwice','Success':True,'Previous':self.__ltwice,'New':val,
                               'ErrorMessage':None})
      self.__ltwice = val
    else:
      errorMessage = ("ltwice must be a boolean")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ltwice','Success':False,'Previous':self.__ltwice,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ltwice','ErrorMessage':errorMessage})

  @temperature.setter
  def temperature(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'temperature','Success':True,'Previous':self.__temperature,
                               'New':val,'ErrorMessage':None})
      self.__temperature = val
    else:
      errorMessage("temperature is in K, so must be a positive number.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'temperature','Success':False,'Previous':self.__temperature,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'temperature','ErrorMessage':errorMessage})

  @pressure.setter
  def pressure(self,val):
    if ti.is_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pressure','Success':True,'Previous':self.__pressure,
                               'New':val,'ErrorMessage':None})
      self.__pressure = val
    else:
      errorMessage("pressure must be a number.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pressure','Success':False,'Previous':self.__pressure,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'pressure','ErrorMessage':errorMessage})

  @nchain_mt.setter
  def nchain_mt(self,val):
    if not isinstance(val,oda.oneDimArray):
      # Single numbers not allowed because will always be at least two values (one moltype and ghost)
      if not isinstance(val,list):
        errorMessage = ("To properly set nchain_mt you have a few options. You can always pass it as a "
                        " python list (e.g. mySim.swap.nchain_mt = [1200,600,0])."
                        " This will automatically convert to the special oneDimArray used by the code."
                        " You can also set it as a oneDimArray object yourself, but this is far more "
                        " tedious and you need to be careful that the errorLog, changeLog, location, "
                        " and variable flags are set properly, which involves passing the right "
                        " reference. Don't forget ghost particles!")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchain_mt','Success':False,
                                 'Previous':repr(self.__nchain_mt),'New':repr(val),
                                 'ErrorMessage':errorMessage})
        self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                'Location':self.__location,'Variable':'nchain_mt',
                                'ErrorMessage':errorMessage})
      else:
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="nchain_mt")
        self.__nchain_mt = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchain_mt','Success':True,'Previous':repr(self.__nchain_mt),
                                 'New':repr(val),'ErrorMessage':None})
      self.__nchain_mt = val

  @inix.setter
  def inix(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'inix','Success':True,'Previous':self.__inix,
                               'New':val,'ErrorMessage':None})
      self.__inix = val
    else:
      errorMessage("inix must be a positive integer.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'inix','Success':False,'Previous':self.__inix,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'inix','ErrorMessage':errorMessage})

  @iniy.setter
  def iniy(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iniy','Success':True,'Previous':self.__iniy,
                               'New':val,'ErrorMessage':None})
      self.__iniy = val
    else:
      errorMessage("iniy must be a positive integer.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iniy','Success':False,'Previous':self.__iniy,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iniy','ErrorMessage':errorMessage})

  @iniz.setter
  def iniz(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iniz','Success':True,'Previous':self.__iniz,
                               'New':val,'ErrorMessage':None})
      self.__iniz = val
    else:
      errorMessage("iniz must be a positive integer.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'iniz','Success':False,'Previous':self.__iniz,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'iniz','ErrorMessage':errorMessage})

  @inirot.setter
  def inirot(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'inirot','Success':True,'Previous':self.__inirot,
                               'New':val,'ErrorMessage':None})
      self.__inirot = val
    else:
      errorMessage("inirot must be a positive integer.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'inirot','Success':False,'Previous':self.__inirot,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'inirot','ErrorMessage':errorMessage})

  @inimix.setter
  def inimix(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'inimix','Success':True,'Previous':self.__inimix,
                               'New':val,'ErrorMessage':None})
      self.__inimix = val
    else:
      errorMessage("inimix must be a positive integer.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'inimix','Success':False,'Previous':self.__inimix,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'inimix','ErrorMessage':errorMessage})

  @zshift.setter
  def zshift(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'zshift','Success':True,'Previous':self.__zshift,
                               'New':val,'ErrorMessage':None})
      self.__zshift = val
    else:
      errorMessage("zshift must be a positive number.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'zshift','Success':False,'Previous':self.__zshift,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'zshift','ErrorMessage':errorMessage})

  @dshift.setter
  def dshift(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'dshift','Success':True,'Previous':self.__dshift,
                               'New':val,'ErrorMessage':None})
      self.__dshift = val
    else:
      errorMessage("dshift must be a positive number.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'dshift','Success':False,'Previous':self.__dshift,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'dshift','ErrorMessage':errorMessage})

  @use_linkcell.setter
  def use_linkcell(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'use_linkcell','Success':True,'Previous':self.__use_linkcell,
                               'New':val,'ErrorMessage':None})
      self.__use_linkcell = val
    else:
      errorMessage("use_linkcell must be a boolean.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'use_linkcell','Success':False,'Previous':self.__use_linkcell,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'use_linkcell','ErrorMessage':errorMessage})

  @rintramax.setter
  def rintramax(self,val):
    if ti.is_positive_number(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'rintramax','Success':True,'Previous':self.__rintramax,
                               'New':val,'ErrorMessage':None})
      self.__rintramax = val
    else:
      errorMessage("rintramax must be a positive number.")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'rintramax','Success':False,'Previous':self.__rintramax,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'rintramax','ErrorMessage':errorMessage})
