import datetime
import mc3s_pywrapper.utilities.test_instance as ti

class System:

  def __init__(self,lnpt=None,lgibbs=None,lgrand=None,lvirial=None,losmoticnvt=None,lanes=None,
               lexpee=None,lpbc=None,lpbcx=None,lpbcy=None,lpbcz=None,lfold=None,lexzeo=None,lslit=None,
               lmipsw=None,ldielect=None,lijall=None,lchgall=None,lewald=None,lrecip=None,lcutcm=None,
               ltailc=None,lshift=None,ldual=None,L_Coul_CBMC=None,lneigh=None,L_Ewald_Auto=None,
               lmixlb=None,lmixjo=None,lmixwh=None,lmixkong=None,L_spline=None,L_linear=None,
               L_vib_table=None,L_bend_table=None,L_elect_table=None,L_cbmc_bend=None,lkdtree=None,
               lgraphite=None,lsami=None,lmuir=None,lelect_field=None,lgaro=None,lionic=None,
               changeLog=[],errorLog=[],location=""):
 
    self.__lnpt          = lnpt
    self.__lgibbs        = lgibbs
    self.__lgrand        = lgrand
    self.__lvirial       = lvirial
    self.__lmipsw        = lmipsw
    self.__lexpee        = lexpee
    self.__ldielect      = ldielect
    self.__lijall        = lijall
    self.__lchgall       = lchgall
    self.__lewald        = lewald
    self.__lrecip        = lrecip
    self.__lcutcm        = lcutcm
    self.__ltailc        = ltailc
    self.__lshift        = lshift
    self.__ldual         = ldual
    self.__lneigh        = lneigh
    self.__L_Coul_CBMC   = L_Coul_CBMC
    self.__L_Ewald_Auto  = L_Ewald_Auto
    self.__lmixlb        = lmixlb
    self.__lmixjo        = lmixjo
    self.__lmixwh        = lmixwh
    self.__lmixkong      = lmixkong
    self.__losmoticnvt   = losmoticnvt
    self.__lanes         = lanes
    self.__lpbc          = lpbc
    self.__lpbcx         = lpbcx
    self.__lpbcy         = lpbcy
    self.__lpbcz         = lpbcz
    self.__lfold         = lfold
    self.__lexzeo        = lexzeo
    self.__lslit         = lslit
    self.__lgraphite     = lgraphite
    self.__lsami         = lsami
    self.__lmuir         = lmuir
    self.__lelect_field  = lelect_field
    self.__lgaro         = lgaro
    self.__lionic        = lionic
    self.__L_spline      = L_spline
    self.__L_linear      = L_linear
    self.__L_vib_table   = L_vib_table
    self.__L_bend_table  = L_bend_table
    self.__L_elect_table = L_elect_table
    self.__L_cbmc_bend   = L_cbmc_bend
    self.__lkdtree       = lkdtree
    self.__changeLog     = changeLog
    self.__errorLog      = errorLog
    self.__location      = "{}/System".format(location)

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
  def lvirial(self):
    return self.__lvirial

  @property
  def lmipsw(self):
    return self.__lmipsw

  @property
  def lexpee(self):
    return self.__lexpee

  @property
  def ldielect(self):
    return self.__ldielect

  @property
  def lijall(self):
    return self.__lijall

  @property
  def lchgall(self):
    return self.__lchgall

  @property
  def lewald(self):
    return self.__lewald

  @property
  def lrecip(self):
    return self.__lrecip

  @property
  def lcutcm(self):
    return self.__lcutcm

  @property
  def ltailc(self):
    return self.__ltailc

  @property
  def lshift(self):
    return self.__lshift

  @property
  def L_Coul_CBMC(self):
    return self.__L_Coul_CBMC

  @property
  def L_Ewald_Auto(self):
    return self.__L_Ewald_Auto

  @property
  def lneigh(self):
    return self.__lneigh

  @property
  def lmixlb(self):
    return self.__lmixlb

  @property
  def lmixjo(self):
    return self.__lmixjo

  @property
  def lmixwh(self):
    return self.__lmixwh
 
  @property
  def lmixkong(self):
    return self.__lmixkong

  @property
  def ldual(self):
    return self.__ldual

  @property
  def losmoticnvt(self):
    return self.__losmoticnvt
   
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
  def lelect_field(self):
    return self.__lelect_field

  @property
  def lgaro(self):
    return self.__lgaro

  @property
  def lionic(self):
    return self.__lionic

  @property
  def L_spline(self):
    return self.__L_spline

  @property
  def L_linear(self):
    return self.__L_linear

  @property
  def L_vib_table(self):
    return self.__L_vib_table

  @property
  def L_bend_table(self):
    return self.__L_bend_table

  @property
  def L_elect_table(self):
    return self.__L_elect_table

  @property
  def L_cbmc_bend(self):
    return self.__L_cbmc_bend

  @property
  def lkdtree(self):
    return self.__lkdtree

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def location(self):
    return self.__location

  @lnpt.setter
  def lnpt(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lnpt',
                               'Success':True,'Previous':self.__lnpt,'New':val,'ErrorMessage':None})
      self.__lnpt = val
    else:
      errorMessage = "Error setting value for lnpt. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lnpt',
                               'Success':False,'Previous':self.__lnpt,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lnpt','ErrorMessage':errorMessage})

  @lgibbs.setter
  def lgibbs(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lgibbs',
                               'Success':True,'Previous':self.__lgibbs,'New':val,'ErrorMessage':None})
      self.__lgibbs = val
    else:
      errorMessage = "Error setting value for lgibbs. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lgibbs',
                               'Success':False,'Previous':self.__lgibbs,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lgibbs','ErrorMessage':errorMessage})

  @lgrand.setter
  def lgrand(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lgrand',
                               'Success':True,'Previous':self.__lgrand,'New':val,'ErrorMessage':None})
      self.__lgrand = val
    else:
      errorMessage = "Error setting value for lgrand. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lgrand',
                               'Success':False,'Previous':self.__lgrand,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lgrand','ErrorMessage':errorMessage})

  @lvirial.setter
  def lvirial(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lvirial',
                               'Success':True,'Previous':self.__lvirial,'New':val,'ErrorMessage':None})
      self.__lvirial = val
    else:
      errorMessage = "Error setting value for lvirial. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lvirial',
                               'Success':False,'Previous':self.__lvirial,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lvirial','ErrorMessage':errorMessage})

  @lmipsw.setter
  def lmipsw(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmipsw',
                               'Success':True,'Previous':self.__lmipsw,'New':val,'ErrorMessage':None})
      self.__lmipsw = val
    else:
      errorMessage = "Error setting value for lmipsw. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmipsw',
                               'Success':False,'Previous':self.__lmipsw,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lmipsw','ErrorMessage':errorMessage})

  @lexpee.setter
  def lexpee(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lexpee',
                               'Success':True,'Previous':self.__lexpee,'New':val,'ErrorMessage':None})
      self.__lexpee = val
    else:
      errorMessage = "Error setting value for lexpee. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lexpee',
                               'Success':False,'Previous':self.__lexpee,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lexpee','ErrorMessage':errorMessage})

  @ldielect.setter
  def ldielect(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'ldielect',
                               'Success':True,'Previous':self.__ldielect,'New':val,'ErrorMessage':None})
      self.__ldielect = val
    else:
      errorMessage = "Error setting value for ldielect. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'ldielect',
                               'Success':False,'Previous':self.__ldielect,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ldielect','ErrorMessage':errorMessage})

  @lijall.setter
  def lijall(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lijall',
                               'Success':True,'Previous':self.__lijall,'New':val,'ErrorMessage':None})
      self.__lijall = val
    else:
      errorMessage = "Error setting value for lijall. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lijall',
                               'Success':False,'Previous':self.__lijall,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lijall','ErrorMessage':errorMessage})

  @lchgall.setter
  def lchgall(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lchgall',
                               'Success':True,'Previous':self.__lchgall,'New':val,'ErrorMessage':None})
      self.__lchgall = val
    else:
      errorMessage = "Error setting value for lchgall. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lchgall',
                               'Success':False,'Previous':self.__lchgall,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lchgall','ErrorMessage':errorMessage})

  @lewald.setter
  def lewald(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lewald',
                               'Success':True,'Previous':self.__lewald,'New':val,'ErrorMessage':None})
      self.__lewald = val
    else:
      errorMessage = "Error setting value for lewald. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lewald',
                               'Success':False,'Previous':self.__lewald,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lewald','ErrorMessage':errorMessage})

  @lrecip.setter
  def lrecip(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lrecip',
                               'Success':True,'Previous':self.__lrecip,'New':val,'ErrorMessage':None})
      self.__lrecip = val
    else:
      errorMessage = "Error setting value for lrecip. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lrecip',
                               'Success':False,'Previous':self.__lrecip,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lrecip','ErrorMessage':errorMessage})

  @lcutcm.setter
  def lcutcm(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lcutcm',
                               'Success':True,'Previous':self.__lcutcm,'New':val,'ErrorMessage':None})
      self.__lcutcm = val
    else:
      errorMessage = "Error setting value for lcutcm. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lcutcm',
                               'Success':False,'Previous':self.__lcutcm,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lcutcm','ErrorMessage':errorMessage})

  @ltailc.setter
  def ltailc(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'ltailc',
                               'Success':True,'Previous':self.__ltailc,'New':val,'ErrorMessage':None})
      self.__ltailc = val
    else:
      errorMessage = "Error setting value for ltailc. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'ltailc',
                               'Success':False,'Previous':self.__ltailc,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ltailc','ErrorMessage':errorMessage})

  @lshift.setter
  def lshift(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lshift',
                               'Success':True,'Previous':self.__lshift,'New':val,'ErrorMessage':None})
      self.__lshift = val
    else:
      errorMessage = "Error setting value for lshift. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lshift',
                               'Success':False,'Previous':self.__lshift,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lshift','ErrorMessage':errorMessage})

  @ldual.setter
  def ldual(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'ldual',
                               'Success':True,'Previous':self.__ldual,'New':val,'ErrorMessage':None})
      self.__ldual = val
    else:
      errorMessage = "Error setting value for ldual. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'ldual',
                               'Success':False,'Previous':self.__ldual,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ldual','ErrorMessage':errorMessage})

  @L_Coul_CBMC.setter
  def L_Coul_CBMC(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_Coul_CBMC',
                               'Success':True,'Previous':self.__L_Coul_CBMC,'New':val,'ErrorMessage':None})
      self.__L_Coul_CBMC = val
    else:
      errorMessage = "Error setting value for L_Coul_CBMC. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_Coul_CBMC',
                               'Success':False,'Previous':self.__L_Coul_CBMC,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'L_Coul_CBMC','ErrorMessage':errorMessage})

  @L_Ewald_Auto.setter
  def L_Ewald_Auto(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_Ewald_Auto',
                               'Success':True,'Previous':self.__L_Ewald_Auto,'New':val,'ErrorMessage':None})
      self.__L_Ewald_Auto = val
    else:
      errorMessage = "Error setting value for L_Ewald_Auto. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_Ewald_Auto',
                               'Success':False,'Previous':self.__L_Ewald_Auto,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'L_Ewald_Auto','ErrorMessage':errorMessage})

  @lneigh.setter
  def lneigh(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lneigh',
                               'Success':True,'Previous':self.__lneigh,'New':val,'ErrorMessage':None})
      self.__lneigh = val
    else:
      errorMessage = "Error setting value for lneigh. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lneigh',
                               'Success':False,'Previous':self.__lneigh,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lneigh','ErrorMessage':errorMessage})

  @lmixlb.setter
  def lmixlb(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmixlb',
                               'Success':True,'Previous':self.__lmixlb,'New':val,'ErrorMessage':None})
      self.__lmixlb = val
    else:
      errorMessage = "Error setting value for lmixlb. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmixlb',
                               'Success':False,'Previous':self.__lmixlb,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lmixlb','ErrorMessage':errorMessage})

  @lmixjo.setter
  def lmixjo(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmixjo',
                               'Success':True,'Previous':self.__lmixjo,'New':val,'ErrorMessage':None})
      self.__lmixjo = val
    else:
      errorMessage = "Error setting value for lmixjo. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmixjo',
                               'Success':False,'Previous':self.__lmixjo,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lmixjo','ErrorMessage':errorMessage})

  @lmixwh.setter
  def lmixwh(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmixwh',
                               'Success':True,'Previous':self.__lmixwh,'New':val,'ErrorMessage':None})
      self.__lmixwh = val
    else:
      errorMessage = "Error setting value for lmixwh. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmixwh',
                               'Success':False,'Previous':self.__lmixwh,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lmixwh','ErrorMessage':errorMessage})

  @lmixkong.setter
  def lmixkong(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmixkong',
                               'Success':True,'Previous':self.__lmixkong,'New':val,'ErrorMessage':None})
      self.__lmixkong = val
    else:
      errorMessage = "Error setting value for lmixkong. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmixkong',
                               'Success':False,'Previous':self.__lmixkong,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lmixkong','ErrorMessage':errorMessage})

  @losmoticnvt.setter
  def losmoticnvt(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                'Variable':'losmoticnvt','Success':True,'Previous':self.__losmoticnvt,
                                'New':val,'ErrorMessage':None})
      self.__losmoticnvt = val
    else:
      errorMessage = "Error setting losmoticnvt. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'losmoticnvt','Success':False,'Previous':self.__losmoticnvt,
                               'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'losmoticnvt','ErrorMessage':errorMessage})

  @lanes.setter
  def lanes(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lanes',
                               'Success':True,'Previous':self.__lanes,'New':val,'ErrorMessage':None})
      self.__lanes = val
    else:
      errorMessage = "Error setting lanes. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lanes',
                               'Success':False,'Previous':self.__lanes,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lanes','ErrorMessage':errorMessage})

  @lpbc.setter
  def lpbc(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lpbc',
                               'Success':True,'Previous':self.__lpbc,'New':val,'ErrorMessage':None})
      self.__lpbc = val
    else:
      errorMessage = "Error setting lpbc. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lpbc',
                               'Success':False,'Previous':self.__lpbc,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lpbc','ErrorMessage':errorMessage})

  @lpbcx.setter
  def lpbcx(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lpbcx',
                               'Success':True,'Previous':self.__lpbcx,'New':val,'ErrorMessage':None})
      self.__lpbcx = val
    else:
      errorMessage = "Error setting lpbcx. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lpbcx',
                               'Success':False,'Previous':self.__lpbcx,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lpbcx','ErrorMessage':errorMessage})

  @lpbcy.setter
  def lpbcy(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lpbcy',
                               'Success':True,'Previous':self.__lpbcy,'New':val,'ErrorMessage':None})
      self.__lpbcy = val
    else:
      errorMessage = "Error setting lpbcy. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lpbcy',
                               'Success':False,'Previous':self.__lpbcy,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lpbcy','ErrorMessage':errorMessage})

  @lpbcz.setter
  def lpbcz(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lpbcz',
                               'Success':True,'Previous':self.__lpbcz,'New':val,'ErrorMessage':None})
      self.__lpbcz = val
    else:
      errorMessage = "Error setting lpbcz. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lpbcz',
                               'Success':False,'Previous':self.__lpbcz,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lpbcz','ErrorMessage':errorMessage})

  @lfold.setter
  def lfold(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lfold',
                               'Success':True,'Previous':self.__lfold,'New':val,'ErrorMessage':None})
      self.__lfold = val
    else:
      errorMessage = "Error setting lfold. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lfold',
                               'Success':False,'Previous':self.__lfold,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lfold','ErrorMessage':errorMessage})

  @lexzeo.setter
  def lexzeo(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lexzeo',
                               'Success':True,'Previous':self.__lexzeo,'New':val,'ErrorMessage':None})
      self.__lexzeo = val
    else:
      errorMessage = "Error setting lexzeo. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lexzeo',
                               'Success':False,'Previous':self.__lexzeo,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lexzeo','ErrorMessage':errorMessage})

  @lslit.setter
  def lslit(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lslit',
                               'Success':True,'Previous':self.__lslit,'New':val,'ErrorMessage':None})
      self.__lslit = val
    else:
      errorMessage = "Error setting lslit. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lslit',
                               'Success':False,'Previous':self.__lslit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lslit','ErrorMessage':errorMessage})

  @lgraphite.setter
  def lgraphite(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lgraphite',
                               'Success':True,'Previous':self.__lgraphite,'New':val,'ErrorMessage':None})
      self.__lgraphite = val
    else:
      errorMessage = "Error setting lgraphite. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lgraphite',
                               'Success':False,'Previous':self.__lgraphite,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lgraphite','ErrorMessage':errorMessage})

  @lsami.setter
  def lsami(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lsami',
                               'Success':True,'Previous':self.__lsami,'New':val,'ErrorMessage':None})
      self.__lsami = val
    else:
      errorMessage = "Error setting lsami. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lsami',
                               'Success':False,'Previous':self.__lsami,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lsami','ErrorMessage':errorMessage})

  @lmuir.setter
  def lmuir(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmuir',
                               'Success':True,'Previous':self.__lmuir,'New':val,'ErrorMessage':None})
      self.__lmuir = val
    else:
      errorMessage = "Error setting lmuir. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lmuir',
                               'Success':False,'Previous':self.__lmuir,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lmuir','ErrorMessage':errorMessage})

  @lelect_field.setter
  def lelect_field(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lelect_field','Success':True,
                               'Previous':self.__lelect_field,'New':val,'ErrorMessage':None})
      self.__lelect_field = val
    else:
      errorMessage = "Error setting lelect_field. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lelect_field','Success':False,
                               'Previous':self.__lelect_field,'New':val,'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lelect_field','ErrorMessage':errorMessage})

  @lgaro.setter
  def lgaro(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lgaro',
                               'Success':True,'Previous':self.__lgaro,'New':val,'ErrorMessage':None})
      self.__lgaro = val
    else:
      errorMessage = "Error setting lgaro. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lgaro','Success':False,'Previous':self.__lgaro,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lgaro','ErrorMessage':errorMessage})

  @lionic.setter
  def lionic(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lionic',
                               'Success':True,'Previous':self.__lionic,'New':val,'ErrorMessage':None})
      self.__lionic=val
    else:
      errorMessage = "Error setting lionic. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lionic',
                               'Success':False,'Previous':self.__lionic,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lionic','ErrorMessage':errorMessage})

  @L_spline.setter
  def L_spline(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_spline',
                               'Success':True,'Previous':self.__L_spline,'New':val,'ErrorMessage':None})
      self.__L_spline = val
    else:
      errorMessage = "Error setting L_spline. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_spline',
                               'Success':False,'Previous':self.__L_spline,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'L_spline','ErrorMessage':errorMessage})

  @L_linear.setter
  def L_linear(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_linear',
                               'Success':True,'Previous':self.__L_linear,'New':val,'ErrorMessage':None})
      self.__L_linear = val
    else:
      errorMessage = "Error setting L_linear. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_linear',
                               'Success':False,'Previous':self.__L_linear,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'L_linear','ErrorMessage':errorMessage})

  @L_vib_table.setter
  def L_vib_table(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_vib_table',
                               'Success':True,'Previous':self.__L_vib_table,'New':val,'ErrorMessage':None})
      self.__L_vib_table = val
    else:
      errorMessage = "Error setting L_vib_table. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_vib_table',
                               'Success':False,'Previous':self.__L_vib_table,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'L_vib_table','ErrorMessage':errorMessage})

  @L_bend_table.setter
  def L_bend_table(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_bend_table',
                               'Success':True,'Previous':self.__L_bend_table,'New':val,'ErrorMessage':None})
      self.__L_bend_table = val
    else:
      errorMessage = "Error setting L_bend_table. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_bend_table',
                               'Success':False,'Previous':self.__L_bend_table,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'L_bend_table','ErrorMessage':errorMessage})

  @L_elect_table.setter
  def L_elect_table(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_elect_table',
                               'Success':True,'Previous':self.__L_elect_table,'New':val,'ErrorMessage':None})
      self.__L_elect_table = val
    else:
      errorMessage = "Error setting L_elect_table. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_elect_table',
                               'Success':False,'Previous':self.__L_elect_table,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'L_elect_table','ErrorMessage':errorMessage})

  @L_cbmc_bend.setter
  def L_cbmc_bend(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_cbmc_bend',
                               'Success':True,'Previous':self.__L_cbmc_bend,'New':val,'ErrorMessage':None})
      self.__L_cbmc_bend = val
    else:
      errorMessage = "Error setting L_cbmc_bend. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'L_cbmc_bend',
                               'Success':False,'Previous':self.__L_cbmc_bend,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'L_cbmc_bend','ErrorMessage':errorMessage})

  @lkdtree.setter
  def lkdtree(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,'Variable':'lkdtree',
                               'Success':True,'Previous':self.__lkdtree,'New':val,'ErrorMessage':None})
      self.__lkdtree = val
    else:
      errorMessage = "Error setting lkdtree. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lkdtree','Success':False,'Previous':self.__lkdtree,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lkdtree','ErrorMessage':errorMessage})
