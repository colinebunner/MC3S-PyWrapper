import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class CBMC:

  icbdir_vals = [0,1]

  def __init__(self,rcutin=None,pmcb=None,pmcbmt=None,pmall=None,nchoi1=None,nchoi=None,nchoir=None,
               nchoih=None,nchtor=None,nchbna=None,nchbnb=None,icbdir=None,icbsta=None,errorLog=[],
               changeLog=[],location=""):

    self.__rcutin = rcutin
    self.__pmcb   = pmcb
    self.__pmcbmt = pmcbmt
    self.__pmall  = pmall
    self.__nchoi1 = nchoi1
    self.__nchoi  = nchoi
    self.__nchoir = nchoir
    self.__nchoih = nchoih
    self.__nchtor = nchtor
    self.__nchbna = nchbna
    self.__nchbnb = nchbnb
    self.__icbdir = icbdir
    self.__icbsta = icbsta
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = "{}/CBMC".format(location)

  @property
  def rcutin(self):
    return self.__rcutin

  @property
  def pmcb(self):
    return self.__pmcb

  @property
  def pmcbmt(self):
    return self.__pmcbmt

  @property
  def pmall(self):
    return self.__pmall

  @property
  def nchoi1(self):
    return self.__nchoi1

  @property
  def nchoi(self):
    return self.__nchoi

  @property
  def nchoir(self):
    return self.__nchoi

  @property
  def nchoih(self):
    return self.__nchoih

  @property
  def nchtor(self):
    return self.__nchtor

  @property
  def nchbna(self):
    return self.__nchbna

  @property
  def nchbnb(self):
    return self.__nchbnb

  @property
  def icbdir(self):
    return self.__icbdir

  @property
  def icbsta(self):
    return self.__icbsta

  @property
  def errorLog(self):
    return self.__errorLog
 
  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @pmcb.setter
  def pmcb(self,val):
    if ti.is_probability(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pmcb','Success':True,'Previous':self.__pmcb,'New':val,
                               'ErrorMessage':None})

      self.__pmcb = val
    else:
      errorMessage = "pmcb must be a number less than 1."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                               'Variable':'pmcb','Success':False,'Previous':self.__pmcb,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Location':self.__location,
                              'Variable':'pmcb','ErrorMessage':errorMessage})

  @pmcbmt.setter
  def pmcbmt(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_probability(val):
          errorMessage = ("To properly set pmcbmt you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.pmcbmt = [1.0,1.0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as a float/int, but they "
                          " must be less than or equal to 1.0.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'pmcbmt','Success':False,'Previous':repr(self.__pmcbmt),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'pmcbmt',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="pmcbmt")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'pmcbmt','Success':True,'Previous':repr(self.__pmcbmt),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__pmcbmt = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'pmcbmt','Success':True,'Previous':repr(self.__pmcbmt),
                                 'New':repr(val),'ErrorMessage':None})
      self.__pmcbmt = val

  @nchoi1.setter
  def nchoi1(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_positive_integer(val):
          errorMessage = ("To properly set nchoi1 you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.nchoi1 = [16,16])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'nchoi1','Success':False,'Previous':repr(self.__nchoi1),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'nchoi1',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="nchoi1")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchoi1','Success':True,'Previous':repr(self.__nchoi1),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__nchoi1 = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchoi1','Success':True,'Previous':repr(self.__nchoi1),
                                 'New':repr(val),'ErrorMessage':None})
      self.__nchoi1 = val

  @nchoi.setter
  def nchoi(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_positive_integer(val):
          errorMessage = ("To properly set nchoi you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.nchoi = [16,16])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'nchoi','Success':False,'Previous':repr(self.__nchoi),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'nchoi',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="nchoi")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchoi','Success':True,'Previous':repr(self.__nchoi),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__nchoi = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchoi','Success':True,'Previous':repr(self.__nchoi),
                                 'New':repr(val),'ErrorMessage':None})
      self.__nchoi = val

  @nchoir.setter
  def nchoir(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_positive_integer(val):
          errorMessage = ("To properly set nchoir you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.nchoir = [16,16])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'nchoir','Success':False,'Previous':repr(self.__nchoir),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'nchoir',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="nchoir")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchoir','Success':True,'Previous':repr(self.__nchoir),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__nchoir = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchoir','Success':True,'Previous':repr(self.__nchoir),
                                 'New':repr(val),'ErrorMessage':None})
      self.__nchoir = val
 
  @nchoih.setter
  def nchoih(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_positive_integer(val):
          errorMessage = ("To properly set nchoih you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.nchoih = [16,16])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'nchoih','Success':False,'Previous':repr(self.__nchoih),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'nchoih',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="nchoih")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchoih','Success':True,'Previous':repr(self.__nchoih),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__nchoih = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchoih','Success':True,'Previous':repr(self.__nchoih),
                                 'New':repr(val),'ErrorMessage':None})
      self.__nchoih = val

  @nchtor.setter
  def nchtor(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_positive_integer(val):
          errorMessage = ("To properly set nchtor you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.nchtor = [16,16])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'nchtor','Success':False,'Previous':repr(self.__nchtor),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'nchtor',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="nchtor")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchtor','Success':True,'Previous':repr(self.__nchtor),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__nchtor = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchtor','Success':True,'Previous':repr(self.__nchtor),
                                 'New':repr(val),'ErrorMessage':None})
      self.__nchtor = val

  @nchbna.setter
  def nchbna(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_positive_integer(val):
          errorMessage = ("To properly set nchbna you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.nchbna = [16,16])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'nchbna','Success':False,'Previous':repr(self.__nchbna),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'nchbna',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="nchbna")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchbna','Success':True,'Previous':repr(self.__nchbna),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__nchbna = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchbna','Success':True,'Previous':repr(self.__nchbna),
                                 'New':repr(val),'ErrorMessage':None})
      self.__nchbna = val

  @nchbnb.setter
  def nchbnb(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_positive_integer(val):
          errorMessage = ("To properly set nchbnb you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.nchbnb = [16,16])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'nchbnb','Success':False,'Previous':repr(self.__nchbnb),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'nchbnb',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="nchbnb")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchbnb','Success':True,'Previous':repr(self.__nchbnb),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__nchbnb = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'nchbnb','Success':True,'Previous':repr(self.__nchbnb),
                                 'New':repr(val),'ErrorMessage':None})
      self.__nchbnb = val

  @icbdir.setter
  def icbdir(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not val in icbdir_vals:
          errorMessage = ("To properly set  you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.icbdir = [0,0])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'icbdir','Success':False,'Previous':repr(self.__icbdir),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'icbdir',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="icbdir")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'icbdir','Success':True,'Previous':repr(self.__icbdir),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__icbdir = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'icbdir','Success':True,'Previous':repr(self.__icbdir),
                                 'New':repr(val),'ErrorMessage':None})
      self.__icbdir = val

  @icbsta.setter
  def icbsta(self,val):
    if not isinstance(val,oda.oneDimArray):
      if not isinstance(val,list):
        # Single numbers are OK
        if not ti.is_integer(val):
          errorMessage = ("To properly set  you have a few options. You can always pass it as a "
                          " python list (e.g. mySim.swap.icbsta = [-5,2])."
                          " This will automatically convert to the special oneDimArray used by the code."
                          " You can also set it as a oneDimArray object yourself, but this is far more "
                          " tedious and you need to be careful that the errorLog, changeLog, location, "
                          " and variable flags are set properly, which involves passing the right "
                          " reference. Note that single values can be passed as an int.")
          self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                   'Variable':'icbsta','Success':False,'Previous':repr(self.__icbsta),
                                   'New':repr(val),'ErrorMessage':errorMessage})
          self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter',
                                  'Location':self.__location,'Variable':'icbsta',
                                  'ErrorMessage':errorMessage})
      else:
        # For single values, cast to list
        val = list(val)
        myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                          location=self.__location,var="icbsta")
        self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'icbsta','Success':True,'Previous':repr(self.__icbsta),
                                 'New':repr(myODA),'ErrorMessage':None})
        self.__icbsta = myODA
    else:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Location':self.__location,
                                 'Variable':'icbsta','Success':True,'Previous':repr(self.__icbsta),
                                 'New':repr(val),'ErrorMessage':None})
      self.__icbsta = val
