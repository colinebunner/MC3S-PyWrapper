from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class GCMC:

    def __init__(
        self,nequil=None,ninstf=None,ninsth=None,ndumph=None,B=None,
        errorLog=[],changeLog=[],location=""
    ):

        self.__nequil = nequil
        self.__ninstf = ninstf
        self.__ninsth = ninsth
        self.__ndumph = ndumph
        self.__B = B
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/gcmc".format(location)


    @property
    def nequil(self):
        return self.__nequil

    @property
    def ninstf(self):
        return self.__ninstf

    @property
    def ninsth(self):
        return self.__ninsth

    @property
    def ndumph(self):
        return self.__ndumph

    @property
    def B(self):
        return self.__B

    @nequil.setter
    def nequil(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "nequil failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nequil", False, repr(getattr(self, "nequil")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nequil", False, repr(getattr(self, "nequil")), repr(val),
                    None
                )
            )
            self.__nequil = val

    @ninstf.setter
    def ninstf(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "ninstf failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ninstf", False, repr(getattr(self, "ninstf")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ninstf", False, repr(getattr(self, "ninstf")), repr(val),
                    None
                )
            )
            self.__ninstf = val

    @ninsth.setter
    def ninsth(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "ninsth failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ninsth", False, repr(getattr(self, "ninsth")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ninsth", False, repr(getattr(self, "ninsth")), repr(val),
                    None
                )
            )
            self.__ninsth = val

    @ndumph.setter
    def ndumph(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "ndumph failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ndumph", False, repr(getattr(self, "ndumph")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ndumph", False, repr(getattr(self, "ndumph")), repr(val),
                    None
                )
            )
            self.__ndumph = val

    @B.setter
    def B(self, val):

        var = "B"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_number(val)):
                errorMessage = logging.multidimensional_error("B", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "B", False, repr(getattr(self, "B")), repr(val),
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
                        self.__location, "B", False, repr(getattr(self, "B")), repr(val),
                        None
                    )
                )
                self.__B = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "B", False, repr(getattr(self, "B")), repr(val),
                    None
                )
            )
            self.__B = val

