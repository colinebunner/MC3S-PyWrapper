from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class Swatch:

    def __init__(
        self,pmswat=None,nswaty=None,pmsatc=None,errorLog=[],changeLog=[],
        location=""
    ):

        self.__pmswat = pmswat
        self.__nswaty = nswaty
        self.__pmsatc = pmsatc
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/swatch".format(location)


    @property
    def pmswat(self):
        return self.__pmswat

    @property
    def nswaty(self):
        return self.__nswaty

    @property
    def pmsatc(self):
        return self.__pmsatc

    @pmswat.setter
    def pmswat(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmswat failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmswat", False, repr(getattr(self, "pmswat")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmswat", False, repr(getattr(self, "pmswat")), repr(val),
                    None
                )
            )
            self.__pmswat = val

    @nswaty.setter
    def nswaty(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "nswaty failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nswaty", False, repr(getattr(self, "nswaty")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nswaty", False, repr(getattr(self, "nswaty")), repr(val),
                    None
                )
            )
            self.__nswaty = val

    @pmsatc.setter
    def pmsatc(self, val):

        var = "pmsatc"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmsatc", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmsatc", False, repr(getattr(self, "pmsatc")), repr(val),
                        errorMessage
                    )
                )
                self.__errorLog.append(
                    logging.errorlog_entry("Setter", errorMessage)
                )
            else:
                if not isinstance(val,list):
                    val = [val]
                myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,
                                location=self.__location,var=var)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmsatc", False, repr(getattr(self, "pmsatc")), repr(val),
                        None
                    )
                )
                self.__pmsatc = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmsatc", False, repr(getattr(self, "pmsatc")), repr(val),
                    None
                )
            )
            self.__pmsatc = val

