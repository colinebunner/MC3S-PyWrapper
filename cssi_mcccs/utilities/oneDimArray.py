class oneDimArray(object):

  def __init__(self,length,errorLog=[],changeLog=[],location="",var=""):
    self.__data      = {i+1:None for i in range(length)}
    self.__length    = length
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = location
    self.__var       = var

  def __getitem__(self,pos):
    if type(pos) != int:
      errorMessage = "Index must be an integer."
      self.__errorLog.append({"ErrorMessage":errorMessage,'Location':self.__location,'Variable':self.__var})
      raise IndexError(errorMessage)
    elif  self.__length < pos < 0:
      errorMessage = "Index out of bounds."
      self.__errorLog.append({"ErrorMessage":errorMessage,'Location':self.__location,'Variable':self.__var})
      raise IndexError(errorMessage)
    else:
      return self.__data[pos]
      

  def __setitem__(self,pos,val):
    if type(pos) != int:
      errorMessage = "Index must be an integer."
      self.__errorLog.append({"ErrorMessage":errorMessage,'Location':self.__location,'Variable':self.__var})
      raise IndexError(errorMessage)
    elif  self.__length < pos < 0:
      errorMessage = "Index out of bounds."
      self.__errorLog.append({"ErrorMessage":errorMessage,'Location':self.__location,'Variable':self.__var})
      raise IndexError(errorMessage)
    else:
      self.__changeLog.append({'Location':self.__location,'Variable':self.__var,'New':val,'Previous':self.__data[pos]})
      self.__data[pos] = val

  def __repr__(self):
    rep = '['
    for i in range(self.__length-1):
      rep += '{:<f}, '.format(self.__data[i+1])
    rep += '{:<f}]'.format(self.__data[self.__length])
    return rep

  @classmethod
  def listToData(cls,val):
    length = len(val)
    return {i+1:val[i] for i in range(length)}

  @classmethod
  def listToODA(cls,val,errorLog=[],changeLog=[],location="",var=""):
    length = len(val)
    myODA = oneDimArray(length=length,errorLog=errorLog,changeLog=changeLog,location=location,var=var)
    myODA.__data = oneDimArray.listToData(val)
    return myODA

  def dataAsArray(self):
    return [self.__data[i+1] for i in range(self.__length)]

  @property
  def data(self):
    return self.__data

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @property
  def location(self):
    return self.__location

  @property
  def var(self):
    return self.__var

  @property
  def length(self):
    return self.__length

  @data.setter
  def data(self,val):
    if type(val) != dict:
      errorMessage = "Data must be a specific dictionary format. Are you sure you know what you are doing?"
      self.__errorLog.append({"ErrorMessage":errorMessage,'Location':self.__location,'Variable':self.__var})
      raise ValueError("This douchebag tried to set oda data but failed")
    else:
      self.__changeLog.append({'Location':self.__location,'Variable':self.__var,'New':self.__val,'Previous':self.__data[pos]})
      self.__data = val
