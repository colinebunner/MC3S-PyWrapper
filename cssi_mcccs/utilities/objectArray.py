from cssi_mcccs.utilities import oneDimArray as oda

class objectArray(oda.oneDimArray):

  def __init__(self,length,errorLog=[],changeLog=[],location="",var=""):
    
    super().__init__(length,errorLog=errorLog,changeLog=changeLog,location=location,var=var)

  def __getitem__(self,pos):
    if type(pos) != int:
      errorMessage = "Index must be an integer."
      self._errorLog.append({"ErrorMessage":errorMessage,'Location':self._location,'Variable':self._var})
      raise IndexError(errorMessage)
    elif  self._length < pos < 0:
      errorMessage = "Index out of bounds."
      self._errorLog.append({"ErrorMessage":errorMessage,'Location':self._location,'Variable':self._var})
      raise IndexError(errorMessage)
    else:
      return self._data[pos]

  def __setitem__(self, pos, val):
    raise TypeError("Don't do that , it's not doing what you think.")

  @classmethod
  def listToOBA(cls,val,errorLog=[],changeLog=[],location="",var=""):
    length = len(val)
    myOBA = objectArray(length=length,errorLog=errorLog,changeLog=changeLog,location=location,var=var)
    myOBA._data = super().listToData(val)
    return myOBA

  @property
  def length(self):
    return self._length

  @property
  def data(self):
    return self._data
