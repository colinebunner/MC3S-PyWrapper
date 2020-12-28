from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class Flucq:

    def __init__(
        self,taflcq=None,fqtemp=None,rmflucq=None,pmflcq=None,pmfqmt=None,
        lflucq=None,lqtrans=None,fqegp=None,nchoiq=None,nswapq=None,
        errorLog=[],changeLog=[],location=""
    ):

        self.__taflcq = taflcq
        self.__fqtemp = fqtemp
        self.__rmflucq = rmflucq
        self.__pmflcq = pmflcq
        self.__pmfqmt = pmfqmt
        self.__lflucq = lflucq
        self.__lqtrans = lqtrans
        self.__fqegp = fqegp
        self.__nchoiq = nchoiq
        self.__nswapq = nswapq
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/flucq".format(location)


    @property
    def taflcq(self):
        return self.__taflcq

    @property
    def fqtemp(self):
        return self.__fqtemp

    @property
    def rmflucq(self):
        return self.__rmflucq

    @property
    def pmflcq(self):
        return self.__pmflcq

    @property
    def pmfqmt(self):
        return self.__pmfqmt

    @property
    def lflucq(self):
        return self.__lflucq

    @property
    def lqtrans(self):
        return self.__lqtrans

    @property
    def fqegp(self):
        return self.__fqegp

    @property
    def nchoiq(self):
        return self.__nchoiq

    @property
    def nswapq(self):
        return self.__nswapq

    @taflcq.setter
    def taflcq(self,val):
        if not ti.is_probability(val):
            errorMessage = "taflcq failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "taflcq", False, repr(getattr(self, "taflcq")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "taflcq", False, repr(getattr(self, "taflcq")), repr(val),
                    None
                )
            )
            self.__taflcq = val

    @fqtemp.setter
    def fqtemp(self,val):
        if not ti.is_number(val):
            errorMessage = "fqtemp failed test_instance.is_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "fqtemp", False, repr(getattr(self, "fqtemp")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "fqtemp", False, repr(getattr(self, "fqtemp")), repr(val),
                    None
                )
            )
            self.__fqtemp = val

    @rmflucq.setter
    def rmflucq(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "rmflucq failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rmflucq", False, repr(getattr(self, "rmflucq")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rmflucq", False, repr(getattr(self, "rmflucq")), repr(val),
                    None
                )
            )
            self.__rmflucq = val

    @pmflcq.setter
    def pmflcq(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmflcq failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmflcq", False, repr(getattr(self, "pmflcq")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmflcq", False, repr(getattr(self, "pmflcq")), repr(val),
                    None
                )
            )
            self.__pmflcq = val

    @pmfqmt.setter
    def pmfqmt(self, val):

        var = "pmfqmt"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmfqmt", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmfqmt", False, repr(getattr(self, "pmfqmt")), repr(val),
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
                        self.__location, "pmfqmt", False, repr(getattr(self, "pmfqmt")), repr(val),
                        None
                    )
                )
                self.__pmfqmt = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmfqmt", False, repr(getattr(self, "pmfqmt")), repr(val),
                    None
                )
            )
            self.__pmfqmt = val

    @lflucq.setter
    def lflucq(self, val):

        var = "lflucq"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_boolean(val)):
                errorMessage = logging.multidimensional_error("lflucq", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "lflucq", False, repr(getattr(self, "lflucq")), repr(val),
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
                        self.__location, "lflucq", False, repr(getattr(self, "lflucq")), repr(val),
                        None
                    )
                )
                self.__lflucq = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lflucq", False, repr(getattr(self, "lflucq")), repr(val),
                    None
                )
            )
            self.__lflucq = val

    @lqtrans.setter
    def lqtrans(self, val):

        var = "lqtrans"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_boolean(val)):
                errorMessage = logging.multidimensional_error("lqtrans", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "lqtrans", False, repr(getattr(self, "lqtrans")), repr(val),
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
                        self.__location, "lqtrans", False, repr(getattr(self, "lqtrans")), repr(val),
                        None
                    )
                )
                self.__lqtrans = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lqtrans", False, repr(getattr(self, "lqtrans")), repr(val),
                    None
                )
            )
            self.__lqtrans = val

    @fqegp.setter
    def fqegp(self, val):

        var = "fqegp"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_number(val)):
                errorMessage = logging.multidimensional_error("fqegp", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "fqegp", False, repr(getattr(self, "fqegp")), repr(val),
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
                        self.__location, "fqegp", False, repr(getattr(self, "fqegp")), repr(val),
                        None
                    )
                )
                self.__fqegp = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "fqegp", False, repr(getattr(self, "fqegp")), repr(val),
                    None
                )
            )
            self.__fqegp = val

    @nchoiq.setter
    def nchoiq(self, val):

        var = "nchoiq"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("nchoiq", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "nchoiq", False, repr(getattr(self, "nchoiq")), repr(val),
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
                        self.__location, "nchoiq", False, repr(getattr(self, "nchoiq")), repr(val),
                        None
                    )
                )
                self.__nchoiq = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nchoiq", False, repr(getattr(self, "nchoiq")), repr(val),
                    None
                )
            )
            self.__nchoiq = val

    @nswapq.setter
    def nswapq(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "nswapq failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nswapq", False, repr(getattr(self, "nswapq")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nswapq", False, repr(getattr(self, "nswapq")), repr(val),
                    None
                )
            )
            self.__nswapq = val

