import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda
from cssi_mcccs.utilities import objectArray   as oba

class beadBond:

  def __init__(self,junit=None,bondID=None,number=None,errorLog=[],changeLog=[],location=""):
    self.__junit     = junit
    self.__bondID    = bondID
    self.__number    = number
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/beadBond-{}".format(location,number)

  @property
  def junit(self):
    return self.__junit

  @property
  def bondID(self):
    return self.__bondID

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

  @junit.setter
  def junit(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'junit','Success':True,'Previous':self.__junit,'New':val,
                               'ErrorMessage':None})
      self.__junit = val
    else:
      errorMessage = "junit must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'junit','Success':False,'Previous':self.__junit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'junit','ErrorMessage':errorMessage})

  @bondID.setter
  def bondID(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'bondID','Success':True,'Previous':self.__bondID,'New':val,
                               'ErrorMessage':None})
      self.__bondID = val
    else:
      errorMessage = "bondID must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'bondID','Success':False,'Previous':self.__bondID,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'bondID','ErrorMessage':errorMessage})

class beadAngle:

  def __init__(self,junit=None,kunit=None,angleID=None,number=None,errorLog=[],changeLog=[],location=""):
    self.__junit     = junit
    self.__kunit     = kunit
    self.__angleID   = angleID
    self.__number    = number
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/beadAngle-{}".format(location,number)

  @property
  def junit(self):
    return self.__junit

  @property
  def kunit(self):
    return self.__kunit

  @property
  def angleID(self):
    return self.__angleID

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

  @junit.setter
  def junit(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'junit','Success':True,'Previous':self.__junit,'New':val,
                               'ErrorMessage':None})
      self.__junit = val
    else:
      errorMessage = "junit must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'junit','Success':False,'Previous':self.__junit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'junit','ErrorMessage':errorMessage})

  @kunit.setter
  def kunit(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'kunit','Success':True,'Previous':self.__kunit,'New':val,
                               'ErrorMessage':None})
      self.__kunit = val
    else:
      errorMessage = "kunit must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'kunit','Success':False,'Previous':self.__kunit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'kunit','ErrorMessage':errorMessage})

  @angleID.setter
  def angleID(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'angleID','Success':True,'Previous':self.__angleID,'New':val,
                               'ErrorMessage':None})
      self.__angleID = val
    else:
      errorMessage = "angleID must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'angleID','Success':False,'Previous':self.__angleID,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'angleID','ErrorMessage':errorMessage})

class beadDihedral:

  def __init__(self,junit=None,kunit=None,lunit=None,angleID=None,number=None,errorLog=[],changeLog=[],location=""):
    self.__junit        = junit
    self.__kunit        = kunit
    self.__lunit        = lunit
    self.__dihedralID   = angleID
    self.__number       = number
    self.__errorLog     = errorLog
    self.__changeLog    = changeLog
    self.__location     = "{}/beadDihedral-{}".format(location,number)

  @property
  def junit(self):
    return self.__junit

  @property
  def kunit(self):
    return self.__kunit

  @property
  def lunit(self):
    return self.__lunit

  @property
  def dihedralID(self):
    return self.__dihedralID

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

  @junit.setter
  def junit(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'junit','Success':True,'Previous':self.__junit,'New':val,
                               'ErrorMessage':None})
      self.__junit = val
    else:
      errorMessage = "junit must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'junit','Success':False,'Previous':self.__junit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'junit','ErrorMessage':errorMessage})

  @kunit.setter
  def kunit(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'kunit','Success':True,'Previous':self.__kunit,'New':val,
                               'ErrorMessage':None})
      self.__kunit = val
    else:
      errorMessage = "kunit must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'kunit','Success':False,'Previous':self.__kunit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'kunit','ErrorMessage':errorMessage})

  @lunit.setter
  def lunit(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lunit','Success':True,'Previous':self.__lunit,'New':val,
                               'ErrorMessage':None})
      self.__lunit = val
    else:
      errorMessage = "lunit must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'lunit','Success':False,'Previous':self.__lunit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'lunit','ErrorMessage':errorMessage})

  @dihedralID.setter
  def dihedralID(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'dihedralID','Success':True,'Previous':self.__dihedralID,'New':val,
                               'ErrorMessage':None})
      self.__dihedralID = val
    else:
      errorMessage = "dihedralID must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'dihedralID','Success':False,'Previous':self.__dihedralID,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'dihedralID','ErrorMessage':errorMessage})

class Bead:

  def __init__(self,unit=None,ntype=None,leaderq=None,nbonds=None,bonds=None,nangles=None,angles=None,ndihedrals=None,
               dihedrals=None,errorLog=[],changeLog=[],location=""):

    self.__unit         = unit
    self.__ntype        = ntype
    self.__leaderq      = leaderq
    self.__nbonds       = nbonds
    self.__bonds        = bonds
    self.__nangles      = nangles
    self.__angles       = angles
    self.__ndihedrals   = ndihedrals
    self.__dihedrals    = dihedrals
    self.__errorLog     = errorLog
    self.__changeLog    = changeLog
    self.__location     = "{}/bead-{}".format(location,unit)

  def __repr__(self):
    return "Bead-{}".format(unit)

  def init_bonds(self,nbonds=None):
    if nbonds is None:
      nbonds = self.__nbonds

    bbs = []
    for i in range(nbonds):
      bbs.append(beadBond(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,number=i+1))
    self.__bonds = oba.objectArray.listToOBA(bbs,errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,var="bonds")

  def init_angles(self,nangles=None):
    if nangles is None:
      nangles = self.__nangles

    bas = []
    for i in range(nangles):
      bas.append(beadAngle(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,number=i+1))
    self.__angles = oba.objectArray.listToOBA(bas,errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,var="angles")

  def init_dihedrals(self,ndihedrals=None):
    if ndihedrals is None:
      ndihedrals = self.__ndihedrals

    bds = []
    for i in range(ndihedrals):
      bds.append(beadDihedral(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,number=i+1))
    self.__dihedrals = oba.objectArray.listToOBA(bds,errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,var="dihedrals")

  @property
  def unit(self):
    return self.__unit

  @property
  def ntype(self):
    return self.__ntype

  @property
  def leaderq(self):
    return self.__leaderq

  @property
  def nbonds(self):
    return self.__nbonds

  @property
  def bonds(self):
    return self.__bonds

  @property
  def nangles(self):
    return self.__nangles

  @property
  def angles(self):
    return self.__angles

  @property
  def ndihedrals(self):
    return self.__ndihedrals

  @property
  def dihedrals(self):
    return self.__dihedrals

  @unit.setter
  def unit(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'unit','Success':True,'Previous':self.__unit,'New':val,
                               'ErrorMessage':None})
      self.__unit = val
    else:
      errorMessage = "unit must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'unit','Success':False,'Previous':self.__unit,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'unit','ErrorMessage':errorMessage})

  @ntype.setter
  def ntype(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ntype','Success':True,'Previous':self.__ntype,'New':val,
                               'ErrorMessage':None})
      self.__ntype = val
    else:
      errorMessage = "ntype must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ntype','Success':False,'Previous':self.__ntype,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ntype','ErrorMessage':errorMessage})

  @leaderq.setter
  def leaderq(self,val):
    if ti.is_positive_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'leaderq','Success':True,'Previous':self.__leaderq,'New':val,
                               'ErrorMessage':None})
      self.__leaderq = val
    else:
      errorMessage = "leaderq must be a positive integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'leaderq','Success':False,'Previous':self.__leaderq,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'leaderq','ErrorMessage':errorMessage})

  @nbonds.setter
  def nbonds(self,val):
    if ti.is_integer(val) and val >= 0:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nbonds','Success':True,'Previous':self.__nbonds,'New':val,
                               'ErrorMessage':None})
      self.__nbonds = val
    else:
      errorMessage = "nbonds must be an integer greater than or equal to 0."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nbonds','Success':False,'Previous':self.__nbonds,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nbonds','ErrorMessage':errorMessage})

  @bonds.setter
  def bonds(self,val):
    if not isinstance(val,oba.objectArray):
      if not (isinstance(val,list) or isinstance(val,tuple) or (isinstance(val,tuple) and len(val) != 2)):
        errorMessage = ("To properly set bonds you have a few options. You can always pass it as a "
                        " python list (e.g. mySim.mtypes[1].beads[1].bonds = [(2,201),(3,202)])."
                        " This will automatically convert to the special oneDimArray used by the code."
                        " You can also set it as a oneDimArray object yourself, but this is far more "
                        " tedious and you need to be careful that the errorLog, changeLog, location, "
                        " and variable flags are set properly, which involves passing the right "
                        " reference. Note that single values can be passed as a tuple, but they must"
                        " have a length of 2 {e.g. mySim.mtypes[1].beads[1].bonds = (2,201)}.")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'','Success':False,'Previous':repr(self.__bonds),
                                   'New':repr(val),'ErrorMessage':errorMessage})
        self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                'Location':self.__location,'Variable':'bonds',
                                'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        if not isinstance(val,list):
          val = [val]
        length = len(val)
        bbs = []
        for i in range(length):
          bbs.append(beadBond(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,number=i+1))
        myOBA = oba.objectArray.listToOBA(bbs,errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,var="bonds")
        for i in range(length):
          myOBA[i+1].junit  = val[i][0]
          myOBA[i+1].bondID = val[i][1]

        self.__bonds = myOBA

    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'bonds','Success':True,'Previous':repr(self.__bonds),
                                 'New':repr(val),'ErrorMessage':None})
      self.__bonds = val

  @nangles.setter
  def nangles(self,val):
    if ti.is_integer(val) and val >= 0:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nangles','Success':True,'Previous':self.__nangles,'New':val,
                               'ErrorMessage':None})
      self.__nangles = val
    else:
      errorMessage = "nangles must be an integer greater than or equal to 0."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nangles','Success':False,'Previous':self.__nangles,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nangles','ErrorMessage':errorMessage})

  @angles.setter
  def angles(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or isinstance(val,tuple) or (isinstance(val,tuple) and len(val) != 3)):
        errorMessage = ("To properly set angles you have a few options. You can always pass it as a "
                        " python list (e.g. mySim.mtypes[1].beads[1].angles = [(2,3,301),(2,4,302)])."
                        " This will automatically convert to the special oneDimArray used by the code."
                        " You can also set it as a oneDimArray object yourself, but this is far more "
                        " tedious and you need to be careful that the errorLog, changeLog, location, "
                        " and variable flags are set properly, which involves passing the right "
                        " reference. Note that single values can be passed as a tuple, but they must"
                        " have a length of 3 {e.g. mySim.mtypes[1].beads[1].angles = (2,3,301)}.")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'','Success':False,'Previous':repr(self.__angles),
                                 'New':repr(val),'ErrorMessage':errorMessage})
        self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                'Location':self.__location,'Variable':'angles',
                                'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        if not isinstance(val,list):
          val = [val]
        length = len(val)
        bas = []
        for i in range(length):
          bas.append(beadAngle(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,number=i+1))
        myOBA = oba.objectArray.listToOBA(bas,errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,var="angles")
        for i in range(length):
          myOBA[i+1].junit   = val[i][0]
          myOBA[i+1].kunit   = val[i][1]
          myOBA[i+1].angleID = val[i][2]

        self.__angles = myOBA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'angles','Success':True,'Previous':repr(self.__angles),
                                 'New':repr(val),'ErrorMessage':None})
      self.__angles = val

  @ndihedrals.setter
  def ndihedrals(self,val):
    if ti.is_integer(val) and val >= 0:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ndihedrals','Success':True,'Previous':self.__ndihedrals,'New':val,
                               'ErrorMessage':None})
      self.__ndihedrals = val
    else:
      errorMessage = "ndihedrals must be an integer greater than or equal to 0."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ndihedrals','Success':False,'Previous':self.__ndihedrals,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ndihedrals','ErrorMessage':errorMessage})

  @dihedrals.setter
  def dihedrals(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not (isinstance(val,list) or isinstance(val,tuple) or (isinstance(val,tuple) and len(val) != 4)):
        errorMessage = ("To properly set dihedrals you have a few options. You can always pass it as a "
                        " python list (e.g. mySim.mtypes[1].beads[1].dihedrals = [(2,3,4,401),(2,3,5,402)])."
                        " This will automatically convert to the special oneDimArray used by the code."
                        " You can also set it as a oneDimArray object yourself, but this is far more "
                        " tedious and you need to be careful that the errorLog, changeLog, location, "
                        " and variable flags are set properly, which involves passing the right "
                        " reference. Note that single values can be passed as a tuple, but they must"
                        " have a length of 4 {e.g. mySim.mtypes[1].beads[1].dihedrals = (2,3,4,401)}.")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'','Success':False,'Previous':repr(self.__dihedrals),
                                 'New':repr(val),'ErrorMessage':errorMessage})
        self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                'Location':self.__location,'Variable':'dihedrals',
                                'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        if not isinstance(val,list):
          val = [val]
        length = len(val)
        bds = []
        for i in range(length):
          bds.append(beadDihedral(errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,number=i+1))
        myOBA = oba.objectArray.listToOBA(length,errorLog=self.__errorLog,changeLog=self.__changeLog,location=self.__location,var="dihedrals")
        for i in range(length):
          myOBA[i+1].junit   = val[i][0]
          myOBA[i+1].kunit   = val[i][1]
          myOBA[i+1].lunit   = val[i][2]
          myOBA[i+1].angleID = val[i][3]

        self.__angles = myOBA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'dihedrals','Success':True,'Previous':repr(self.__dihedrals),
                                 'New':repr(val),'ErrorMessage':None})
      self.__dihedrals = val
