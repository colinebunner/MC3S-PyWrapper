import datetime
from cssi_mcccs.utilities import test_instance as ti
from cssi_mcccs.utilities import oneDimArray   as oda

class Bead:

  def __init__(self,errorLog=[],changeLog=[],location="",number=None):
    
    self.__errorLog  = errorLog
    self.__changeLog = changeLog
    self.__location  = location
    self.__number    = number

