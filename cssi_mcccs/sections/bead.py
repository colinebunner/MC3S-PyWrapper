import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class Bead:

  def __init__(self,unit=None,ntype=None,leaderq=None,nbond=None,bondList=None,nangle=None,angleList=None,ndihedral=None,
               dihedralList=None,errorLog=[],changeLog=[],location=""):
    
    self.__unit         = unit
    self.__ntype        = ntype
    self.__leaderq      = leaderq
    self.__nbond        = nbond
    self.__bondList     = bondList
    self.__nangle       = nangle
    self.__angleList    = angleList
    self.__ndihedral    = ndihedral
    self.__dihedralList = dihedralList
    self.__errorLog     = errorLog
    self.__changeLog    = changeLog
    self.__location     = "{}/bead-{}".format(location,unit)

  def __repr__(self):
    return "Bead-{}".format(unit)

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
  def nbond(self):
    return self.__nbond

  @property
  def bondList(self):
    return self.__bondList

  @property
  def nangle(self):
    return self.__nangle

  @property
  def angleList(self):
    return self.__angleList
 
  @property
  def ndihedral(self):
    return self.__ndihedral

  @property
  def dihedralList(self):
    return self.__dihedralList

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

  @nbond.setter
  def nbond(self,val):
    if ti.is_integer(val) and val >= 0:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nbond','Success':True,'Previous':self.__nbond,'New':val,
                               'ErrorMessage':None})
      self.__nbond = val
    else:
      errorMessage = "nbond must be an integer greater than or equal to 0."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nbond','Success':False,'Previous':self.__nbond,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nbond','ErrorMessage':errorMessage})
  
  @bondList.setter
  def bondList(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single tuples are OK in the case of one bond
        if not isinstance(val,tuple) or (isinstance(val,tuple) and len(val) != 2):
          errorMessage = ("To properly set bondList you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.mtypes[1].beads[1].bondList = [(2,201),(3,202)])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as a tuple, but they must"
                          " have a length of 2 {e.g. mySim.mtypes[1].beads[1].bondList = (2,201)}.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'','Success':False,'Previous':repr(self.__bondList),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'bondList',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="bondList")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'bondList','Success':True,'Previous':repr(self.__bondList),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__bondList = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'bondList','Success':True,'Previous':repr(self.__bondList),
                                 'New':repr(val),'ErrorMessage':None})
      self.__bondList = val

  @nangle.setter
  def nangle(self,val):
    if ti.is_integer(val) and val >= 0:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nangle','Success':True,'Previous':self.__nangle,'New':val,
                               'ErrorMessage':None})
      self.__nangle = val
    else:
      errorMessage = "nangle must be an integer greater than or equal to 0."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'nangle','Success':False,'Previous':self.__nangle,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'nangle','ErrorMessage':errorMessage})

  @angleList.setter
  def angleList(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single tuples are OK in the case of one bond
        if not isinstance(val,tuple) or (isinstance(val,tuple) and len(val) != 3):
          errorMessage = ("To properly set angleList you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.mtypes[1].beads[1].angleList = [(2,3,301),(2,4,302)])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as a tuple, but they must"
                          " have a length of 3 {e.g. mySim.mtypes[1].beads[1].angleList = (2,3,301)}.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'','Success':False,'Previous':repr(self.__angleList),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'angleList',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="angleList")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'angleList','Success':True,'Previous':repr(self.__angleList),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__angleList = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'angleList','Success':True,'Previous':repr(self.__angleList),
                                 'New':repr(val),'ErrorMessage':None})
      self.__angleList = val

  @ndihedral.setter
  def ndihedral(self,val):
    if ti.is_integer(val) and val >= 0:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ndihedral','Success':True,'Previous':self.__ndihedral,'New':val,
                               'ErrorMessage':None})
      self.__ndihedral = val
    else:
      errorMessage = "ndihedral must be an integer greater than or equal to 0."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'ndihedral','Success':False,'Previous':self.__ndihedral,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'ndihedral','ErrorMessage':errorMessage})

  @dihedralList.setter
  def dihedralList(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single tuples are OK in the case of one bond
        if not isinstance(val,tuple) or (isinstance(val,tuple) and len(val) != 4):
          errorMessage = ("To properly set dihedralList you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.mtypes[1].beads[1].dihedralList = [(2,3,4,401),(2,3,5,402)])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as a tuple, but they must"
                          " have a length of 4 {e.g. mySim.mtypes[1].beads[1].dihedralList = (2,3,4,401)}.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'','Success':False,'Previous':repr(self.__dihedralList),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'dihedralList',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="dihedralList")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'dihedralList','Success':True,'Previous':repr(self.__dihedralList),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__dihedralList = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'dihedralList','Success':True,'Previous':repr(self.__dihedralList),
                                 'New':repr(val),'ErrorMessage':None})
      self.__dihedralList = val
