from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class External_field:

    def __init__(
        self,Elect_field=None,errorLog=[],changeLog=[],location=""
    ):

        self.__Elect_field = Elect_field
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/external_field".format(location)


    @property
    def Elect_field(self):
        return self.__Elect_field

    @Elect_field.setter
    def Elect_field(self,val):
        if not ti.is_number(val):
            errorMessage = "Elect_field failed test_instance.is_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "Elect_field", False, repr(getattr(self, "Elect_field")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "Elect_field", False, repr(getattr(self, "Elect_field")), repr(val),
                    None
                )
            )
            self.__Elect_field = val

