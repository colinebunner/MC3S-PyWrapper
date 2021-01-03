from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class Volume:

    def __init__(
        self,tavol=None,iratv=None,pmvlmt=None,pmvolb=None,box5=None,box6=None,
        pmvol=None,pmvolx=None,pmvoly=None,rmvolume=None,allow_cutoff_failure=None,
        l_bilayer=None,pm_consv=None,pmvol_xy=None,errorLog=[],changeLog=[],location=""
    ):

        self.__tavol = tavol
        self.__iratv = iratv
        self.__pmvlmt = pmvlmt
        self.__pmvolb = pmvolb
        self.__box5 = box5
        self.__box6 = box6
        self.__pmvol = pmvol
        self.__pmvolx = pmvolx
        self.__pmvoly = pmvoly
        self.__rmvolume = rmvolume
        self.__allow_cutoff_failure = allow_cutoff_failure
        self.__l_bilayer = l_bilayer
        self.__pm_consv = pm_consv
        self.__pmvol_xy = pmvol_xy
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/Volume".format(location)


    @property
    def tavol(self):
        return self.__tavol

    @property
    def iratv(self):
        return self.__iratv

    @property
    def pmvlmt(self):
        return self.__pmvlmt

    @property
    def pmvolb(self):
        return self.__pmvolb

    @property
    def box5(self):
        return self.__box5

    @property
    def box6(self):
        return self.__box6

    @property
    def pmvol(self):
        return self.__pmvol

    @property
    def pmvolx(self):
        return self.__pmvolx

    @property
    def pmvoly(self):
        return self.__pmvoly

    @property
    def rmvolume(self):
        return self.__rmvolume

    @property
    def allow_cutoff_failure(self):
        return self.__allow_cutoff_failure

    @property
    def l_bilayer(self):
        return self.__l_bilayer

    @property
    def pm_consv(self):
        return self.__pm_consv

    @property
    def pmvol_xy(self):
        return self.__pmvol_xy

    @tavol.setter
    def tavol(self,val):
        if not ti.is_probability(val):
            errorMessage = "tavol failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "tavol", False, repr(getattr(self, "tavol")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "tavol", False, repr(getattr(self, "tavol")), repr(val),
                    None
                )
            )
            self.__tavol = val

    @iratv.setter
    def iratv(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "iratv failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "iratv", False, repr(getattr(self, "iratv")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "iratv", False, repr(getattr(self, "iratv")), repr(val),
                    None
                )
            )
            self.__iratv = val

    @pmvlmt.setter
    def pmvlmt(self, val):

        var = "pmvlmt"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmvlmt", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmvlmt", False, repr(getattr(self, "pmvlmt")), repr(val),
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
                        self.__location, "pmvlmt", False, repr(getattr(self, "pmvlmt")), repr(val),
                        None
                    )
                )
                self.__pmvlmt = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvlmt", False, repr(getattr(self, "pmvlmt")), repr(val),
                    None
                )
            )
            self.__pmvlmt = val

    @pmvolb.setter
    def pmvolb(self, val):

        var = "pmvolb"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmvolb", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmvolb", False, repr(getattr(self, "pmvolb")), repr(val),
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
                        self.__location, "pmvolb", False, repr(getattr(self, "pmvolb")), repr(val),
                        None
                    )
                )
                self.__pmvolb = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvolb", False, repr(getattr(self, "pmvolb")), repr(val),
                    None
                )
            )
            self.__pmvolb = val

    @box5.setter
    def box5(self, val):

        var = "box5"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("box5", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "box5", False, repr(getattr(self, "box5")), repr(val),
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
                        self.__location, "box5", False, repr(getattr(self, "box5")), repr(val),
                        None
                    )
                )
                self.__box5 = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "box5", False, repr(getattr(self, "box5")), repr(val),
                    None
                )
            )
            self.__box5 = val

    @box6.setter
    def box6(self, val):

        var = "box6"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("box6", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "box6", False, repr(getattr(self, "box6")), repr(val),
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
                        self.__location, "box6", False, repr(getattr(self, "box6")), repr(val),
                        None
                    )
                )
                self.__box6 = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "box6", False, repr(getattr(self, "box6")), repr(val),
                    None
                )
            )
            self.__box6 = val

    @pmvol.setter
    def pmvol(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmvol failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvol", False, repr(getattr(self, "pmvol")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvol", False, repr(getattr(self, "pmvol")), repr(val),
                    None
                )
            )
            self.__pmvol = val

    @pmvolx.setter
    def pmvolx(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmvolx failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvolx", False, repr(getattr(self, "pmvolx")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvolx", False, repr(getattr(self, "pmvolx")), repr(val),
                    None
                )
            )
            self.__pmvolx = val

    @pmvoly.setter
    def pmvoly(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmvoly failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvoly", False, repr(getattr(self, "pmvoly")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvoly", False, repr(getattr(self, "pmvoly")), repr(val),
                    None
                )
            )
            self.__pmvoly = val

    @rmvolume.setter
    def rmvolume(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "rmvolume failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rmvolume", False, repr(getattr(self, "rmvolume")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rmvolume", False, repr(getattr(self, "rmvolume")), repr(val),
                    None
                )
            )
            self.__rmvolume = val

    @allow_cutoff_failure.setter
    def allow_cutoff_failure(self,val):
        if not ti.is_integer(val):
            errorMessage = "allow_cutoff_failure failed test_instance.is_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "allow_cutoff_failure", False, repr(getattr(self, "allow_cutoff_failure")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "allow_cutoff_failure", False, repr(getattr(self, "allow_cutoff_failure")), repr(val),
                    None
                )
            )
            self.__allow_cutoff_failure = val

    @l_bilayer.setter
    def l_bilayer(self,val):
        if not ti.is_boolean(val):
            errorMessage = "l_bilayer failed test_instance.is_boolean check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "l_bilayer", False, repr(getattr(self, "l_bilayer")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "l_bilayer", False, repr(getattr(self, "l_bilayer")), repr(val),
                    None
                )
            )
            self.__l_bilayer = val

    @pm_consv.setter
    def pm_consv(self,val):
        if not ti.is_probability(val):
            errorMessage = "pm_consv failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pm_consv", False, repr(getattr(self, "pm_consv")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pm_consv", False, repr(getattr(self, "pm_consv")), repr(val),
                    None
                )
            )
            self.__pm_consv = val

    @pmvol_xy.setter
    def pmvol_xy(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmvol_xy failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvol_xy", False, repr(getattr(self, "pmvol_xy")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmvol_xy", False, repr(getattr(self, "pmvol_xy")), repr(val),
                    None
                )
            )
            self.__pmvol_xy = val

