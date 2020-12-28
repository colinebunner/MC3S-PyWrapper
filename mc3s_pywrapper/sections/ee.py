from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class Ee:

    def __init__(
        self,pmexpc=None,pmeemt=None,pmexpc1=None,lexpand=None,
        errorLog=[],changeLog=[],location=""
    ):

        self.__pmexpc = pmexpc
        self.__pmeemt = pmeemt
        self.__pmexpc1 = pmexpc1
        self.__lexpand = lexpand
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/ee".format(location)


    @property
    def pmexpc(self):
        return self.__pmexpc

    @property
    def pmeemt(self):
        return self.__pmeemt

    @property
    def pmexpc1(self):
        return self.__pmexpc1

    @property
    def lexpand(self):
        return self.__lexpand

    @pmexpc.setter
    def pmexpc(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmexpc failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmexpc", False, repr(getattr(self, "pmexpc")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmexpc", False, repr(getattr(self, "pmexpc")), repr(val),
                    None
                )
            )
            self.__pmexpc = val

    @pmeemt.setter
    def pmeemt(self, val):

        var = "pmeemt"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmeemt", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmeemt", False, repr(getattr(self, "pmeemt")), repr(val),
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
                        self.__location, "pmeemt", False, repr(getattr(self, "pmeemt")), repr(val),
                        None
                    )
                )
                self.__pmeemt = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmeemt", False, repr(getattr(self, "pmeemt")), repr(val),
                    None
                )
            )
            self.__pmeemt = val

    @pmexpc1.setter
    def pmexpc1(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmexpc1 failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmexpc1", False, repr(getattr(self, "pmexpc1")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmexpc1", False, repr(getattr(self, "pmexpc1")), repr(val),
                    None
                )
            )
            self.__pmexpc1 = val

    @lexpand.setter
    def lexpand(self, val):

        var = "lexpand"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_boolean(val)):
                errorMessage = logging.multidimensional_error("lexpand", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "lexpand", False, repr(getattr(self, "lexpand")), repr(val),
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
                        self.__location, "lexpand", False, repr(getattr(self, "lexpand")), repr(val),
                        None
                    )
                )
                self.__lexpand = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lexpand", False, repr(getattr(self, "lexpand")), repr(val),
                    None
                )
            )
            self.__lexpand = val

