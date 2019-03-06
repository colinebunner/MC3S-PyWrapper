import datetime
import cssi_mcccs.utilities as utilities

class System:

  def __init__(self,lnpt=None,lgibbs=None,lgrand=None,losmotic_nvt=None,lanes=None,lpbc=None,lpbcx=None,
               lpbcy=None,lpbcz=None,lfold=None,lexzeo=None,lslit=None,lgraphite=None,lsami=None,
               lmuir=None,lelect_field=None,lgaro=None,lionic=None,lkdtree=None,changeLog=[],
               errorLog=[]):

    self.__lnpt         = lnpt
    self.__lgibbs       = lgibbs
    self.__lgrand       = lgrand
    self.__losmotic_nvt = losmotic_nvt
    self.__lanes        = lanes
    self.__lpbc         = lpbc
    self.__lpbcx        = lpbcx
    self.__lpbcy        = lpbcy
    self.__lpbcz        = lpbcz
    self.__lfold        = lfold
    self.__lexzeo       = lexzeo
    self.__lslit        = lslit
    self.__lgraphite    = lgraphite
    self.__lsami        = lsami
    self.__lmuir        = lmuir
    self.__lelect_field = lelect_field
    self.__lgaro        = lgaro
    self.__lionic       = lionic
    self.__changeLog    = changeLog
    self.__errorLog     = errorLog

  @property
  def lnpt(self):
    return self.__lnpt
 
  @property
  def lgibbs(self):
    return self.__lgibbs

  @property
  def lgrand(self):
    return self.__lgrand

  @property
  def losmotic_nvt(self):
    return self.__losmotic_nvt
   
  @property
  def lanes(self):
    return self.__lanes

  @property
  def lpbc(self):
    return self.__lpbc

  @property
  def lpbcx(self):
    return self.__lpbcx

  @property
  def lpbcy(self):
    return self.__lpbcy

  @property
  def lpbcz(self):
    return self.__lpbcz

  @property
  def lfold(self):
    return self.__lfold

  @property
  def lexzeo(self):
    return self.__lexzeo

  @property
  def lslit(self):
    return self.__lslit

  @property
  def lgraphite(self):
    return self.__lgraphite

  @property
  def lsami(self):
    return self.__lsami

  @property
  def lmuir(self):
    return self.__lmuir

  @property
  def lelectric_field(self):
    return self.__lelect_field

  @property
  def lgaro(self):
    return self.__lgaro

  @property
  def lionic(self):
    return self.__lionic

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def errorLog(self):
    return self.__errorLog

  @lnpt.setter
  def lnpt(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lnpt',
                               'Success':True,'Previous':self.__lnpt,'New':val,'ErrorMessage':None})
      self.__lnpt = val
    else:
      errorMessage = "Error setting value for lnpt. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lnpt',
                               'Success':False,'Previous':self.__lnpt,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lnpt','ErrorMessage':errorMessage})

  @lgibbs.setter
  def lgibbs(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lgibbs',
                               'Success':True,'Previous':self.__lgibbs,'New':val,'ErrorMessage':None})
      self.__lgibbs = val
    else:
      errorMessage = "Error setting value for lgibbs. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lgibbs',
                               'Success':False,'Previous':self.__lgibbs,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lgibbs','ErrorMessage':errorMessage})

  @lgrand.setter
  def lgrand(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lgrand',
                               'Success':True,'Previous':self.__lgrand,'New':val,'ErrorMessage':None})
      self.__lgrand = val
    else:
      errorMessage = "Error setting value for lgrand. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lgrand',
                               'Success':False,'Previous':self.__lgrand,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lgrand','ErrorMessage':errorMessage})

  @losmotic_nvt.setter
  def losmotic_nvt(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System',
                                'Variable':'losmotic_nvt','Success':True,'Previous':self.__losmotic_nvt,
                                'New':val,'ErrorMessage':None})
      self.__losmotic_nvt = val
    else:
      errorMessage = "Error setting losmotic_nvt. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System',
                               'Variable':'losmotic_nvt','Success':False,'Previous':self.__losmotic_nvt,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'losmotic_nvt','ErrorMessage':errorMessage})

  @lanes.setter
  def lanes(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lanes',
                               'Success':True,'Previous':self.__lanes,'New':val,'ErrorMessage':None})
      self.__lanes = val
    else:
      errorMessage = "Error setting lanes. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lanes',
                               'Success':False,'Previous':self.__lanes,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lanes','ErrorMessage':errorMessage})

  @lpbc.setter
  def lpbc(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lpbc',
                               'Success':True,'Previous':self.__lpbc,'New':val,'ErrorMessage':None})
      self.__lpbc = val
    else:
      errorMessage = "Error setting lpbc. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lpbc',
                               'Success':False,'Previous':self.__lpbc,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lpbc','ErrorMessage':errorMessage})

  @lpbcx.setter
  def lpbcx(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lpbcx',
                               'Success':True,'Previous':self.__lpbcx,'New':val,'ErrorMessage':None})
      self.__lpbcx = val
    else:
      errorMessage = "Error setting lpbcx. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lpbcx',
                               'Success':False,'Previous':self.__lpbcx,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lpbcx','ErrorMessage':errorMessage})

  @lpbcy.setter
  def lpbcy(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lpbcy',
                               'Success':True,'Previous':self.__lpbcy,'New':val,'ErrorMessage':None})
      self.__lpbcy = val
    else:
      errorMessage = "Error setting lpbcy. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lpbcy',
                               'Success':False,'Previous':self.__lpbcy,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lpbcy','ErrorMessage':errorMessage})

  @lpbcz.setter
  def lpbcz(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lpbcz',
                               'Success':True,'Previous':self.__lpbcz,'New':val,'ErrorMessage':None})
      self.__lpbcz = val
    else:
      errorMessage = "Error setting lpbcz. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lpbcz',
                               'Success':False,'Previous':self.__lpbcz,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lpbcz','ErrorMessage':errorMessage})

  @lfold.setter
  def lfold(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lfold',
                               'Success':True,'Previous':self.__lfold,'New':val,'ErrorMessage':None})
      self.__lfold = val
    else:
      errorMessage = "Error setting lfold. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lfold',
                               'Success':False,'Previous':self.__lfold,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lfold','ErrorMessage':errorMessage})

  @lexzeo.setter
  def lexzeo(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lexzeo',
                               'Success':True,'Previous':self.__lexzeo,'New':val,'ErrorMessage':None})
      self.__lexzeo = val
    else:
      errorMessage = "Error setting lexzeo. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lexzeo',
                               'Success':False,'Previous':self.__lexzeo,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lexzeo','ErrorMessage':errorMessage})

  @lslit.setter
  def lslit(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lslit',
                               'Success':True,'Previous':self.__lslit,'New':val,'ErrorMessage':None})
      self.__lslit = val
    else:
      errorMessage = "Error setting lslit. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lslit',
                               'Success':False,'Previous':self.__lslit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lslit','ErrorMessage':errorMessage})

  @lgraphite.setter
  def lgraphite(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lgraphite',
                               'Success':True,'Previous':self.__lgraphite,'New':val,'ErrorMessage':None})
      self.__lgraphite = val
    else:
      errorMessage = "Error setting lgraphite. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lgraphite',
                               'Success':False,'Previous':self.__lgraphite,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lgraphite','ErrorMessage':errorMessage})

  @lsami.setter
  def lsami(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lsami',
                               'Success':True,'Previous':self.__lsami,'New':val,'ErrorMessage':None})
      self.__lsami = val
    else:
      errorMessage = "Error setting lsami. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lsami',
                               'Success':False,'Previous':self.__lsami,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lsami','ErrorMessage':errorMessage})

  @lmuir.setter
  def lmuir(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lmuir',
                               'Success':True,'Previous':self.__lmuir,'New':val,'ErrorMessage':None})
      self.__lmuir = val
    else:
      errorMessage = "Error setting lmuir. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lmuir',
                               'Success':False,'Previous':self.__lmuir,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lmuir','ErrorMessage':errorMessage})

  @lelectric_field.setter
  def lelectric_field(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System',
                               'Variable':'lelectric_field','Success':True,
                               'Previous':self.__lelectric_field,'New':val,'ErrorMessage':None})
      self.__lelect_field = val
    else:
      errorMessage = "Error setting lelectric_field. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System',
                               'Variable':'lelectric_field','Success':False,
                               'Previous':self.__lelectric_field,'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lelectric_field','ErrorMessage':errorMessage})

  @lgaro.setter
  def lgaro(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lgaro',
                               'Success':True,'Previous':self.__lgaro,'New':val,'ErrorMessage':None})
      self.__lgaro = val
    else:
      errorMessage = "Error setting lgaro. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System',
                               'Variable':'lgaro','Success':False,'Previous':self.__lgaro,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lgaro','ErrorMessage':errorMessage})

  @lionic.setter
  def lionic(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lionic',
                               'Success':True,'Previous':self.__lionic,'New':val,'ErrorMessage':None})
      self.__lionic=val
    else:
      errorMessage = "Error setting lionic. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'System','Variable':'lionic',
                               'Success':False,'Previous':self.__lionic,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'System',
                              'Variable':'lionic','ErrorMessage':errorMessage})
