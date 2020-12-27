from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class Simple:

    def __init__(
        self,pm_atom_tra=None,Armtra=None,pmtra=None,pmtrmt=None,rmtra=None,
        tatra=None,pmromt=None,rmrot=None,tarot=None,errorLog=[],changeLog=[],
        location=""
    ):

        self.__pm_atom_tra = pm_atom_tra
        self.__Armtra = Armtra
        self.__pmtra = pmtra
        self.__pmtrmt = pmtrmt
        self.__rmtra = rmtra
        self.__tatra = tatra
        self.__pmromt = pmromt
        self.__rmrot = rmrot
        self.__tarot = tarot
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/simple".format(location)


    @property
    def pm_atom_tra(self):
        return self.__pm_atom_tra

    @property
    def Armtra(self):
        return self.__Armtra

    @property
    def pmtra(self):
        return self.__pmtra

    @property
    def pmtrmt(self):
        return self.__pmtrmt

    @property
    def rmtra(self):
        return self.__rmtra

    @property
    def tatra(self):
        return self.__tatra

    @property
    def pmromt(self):
        return self.__pmromt

    @property
    def rmrot(self):
        return self.__rmrot

    @property
    def tarot(self):
        return self.__tarot

    @pm_atom_tra.setter
    def pm_atom_tra(self,val):
        if not ti.is_probability(val):
            errorMessage = "pm_atom_tra failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pm_atom_tra", False, repr(getattr(self, "pm_atom_tra")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pm_atom_tra", False, repr(getattr(self, "pm_atom_tra")), repr(val),
                    None
                )
            )
            self.__pm_atom_tra = val

    @Armtra.setter
    def Armtra(self, val):

        var = "Armtra"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_number(val)):
                errorMessage = logging.multidimensional_error("Armtra", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "Armtra", False, repr(getattr(self, "Armtra")), repr(val),
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
                        self.__location, "Armtra", False, repr(getattr(self, "Armtra")), repr(val),
                        None
                    )
                )
                self.__Armtra = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "Armtra", False, repr(getattr(self, "Armtra")), repr(val),
                    None
                )
            )
            self.__Armtra = val

    @pmtra.setter
    def pmtra(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmtra failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmtra", False, repr(getattr(self, "pmtra")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmtra", False, repr(getattr(self, "pmtra")), repr(val),
                    None
                )
            )
            self.__pmtra = val

    @pmtrmt.setter
    def pmtrmt(self, val):

        var = "pmtrmt"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmtrmt", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmtrmt", False, repr(getattr(self, "pmtrmt")), repr(val),
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
                        self.__location, "pmtrmt", False, repr(getattr(self, "pmtrmt")), repr(val),
                        None
                    )
                )
                self.__pmtrmt = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmtrmt", False, repr(getattr(self, "pmtrmt")), repr(val),
                    None
                )
            )
            self.__pmtrmt = val

    @rmtra.setter
    def rmtra(self, val):

        var = "rmtra"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_number(val)):
                errorMessage = logging.multidimensional_error("rmtra", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "rmtra", False, repr(getattr(self, "rmtra")), repr(val),
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
                        self.__location, "rmtra", False, repr(getattr(self, "rmtra")), repr(val),
                        None
                    )
                )
                self.__rmtra = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rmtra", False, repr(getattr(self, "rmtra")), repr(val),
                    None
                )
            )
            self.__rmtra = val

    @tatra.setter
    def tatra(self,val):
        if not ti.is_probability(val):
            errorMessage = "tatra failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "tatra", False, repr(getattr(self, "tatra")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "tatra", False, repr(getattr(self, "tatra")), repr(val),
                    None
                )
            )
            self.__tatra = val

    @pmromt.setter
    def pmromt(self, val):

        var = "pmromt"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmromt", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmromt", False, repr(getattr(self, "pmromt")), repr(val),
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
                        self.__location, "pmromt", False, repr(getattr(self, "pmromt")), repr(val),
                        None
                    )
                )
                self.__pmromt = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmromt", False, repr(getattr(self, "pmromt")), repr(val),
                    None
                )
            )
            self.__pmromt = val

    @rmrot.setter
    def rmrot(self, val):

        var = "rmrot"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_number(val)):
                errorMessage = logging.multidimensional_error("rmrot", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "rmrot", False, repr(getattr(self, "rmrot")), repr(val),
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
                        self.__location, "rmrot", False, repr(getattr(self, "rmrot")), repr(val),
                        None
                    )
                )
                self.__rmrot = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rmrot", False, repr(getattr(self, "rmrot")), repr(val),
                    None
                )
            )
            self.__rmrot = val

    @tarot.setter
    def tarot(self,val):
        if not ti.is_probability(val):
            errorMessage = "tarot failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "tarot", False, repr(getattr(self, "tarot")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "tarot", False, repr(getattr(self, "tarot")), repr(val),
                    None
                )
            )
            self.__tarot = val

