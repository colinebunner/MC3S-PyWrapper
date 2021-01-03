from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class CBMC:

    def __init__(
        self,rcutin=None,pmcb=None,pmcbmt=None,pmall=None,nchoi1=None,nchoi=None,
        nchoir=None,nchoih=None,nchtor=None,nchbna=None,nchbnb=None,icbdir=None,
        icbsta=None,rbsmax=None,rbsmin=None,avbmc_version=None,pmbias=None,pmbsmt=None,
        pmbias2=None,errorLog=[],changeLog=[],location=""
    ):

        self.__rcutin = rcutin
        self.__pmcb = pmcb
        self.__pmcbmt = pmcbmt
        self.__pmall = pmall
        self.__nchoi1 = nchoi1
        self.__nchoi = nchoi
        self.__nchoir = nchoir
        self.__nchoih = nchoih
        self.__nchtor = nchtor
        self.__nchbna = nchbna
        self.__nchbnb = nchbnb
        self.__icbdir = icbdir
        self.__icbsta = icbsta
        self.__rbsmax = rbsmax
        self.__rbsmin = rbsmin
        self.__avbmc_version = avbmc_version
        self.__pmbias = pmbias
        self.__pmbsmt = pmbsmt
        self.__pmbias2 = pmbias2
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/CBMC".format(location)


    @property
    def rcutin(self):
        return self.__rcutin

    @property
    def pmcb(self):
        return self.__pmcb

    @property
    def pmcbmt(self):
        return self.__pmcbmt

    @property
    def pmall(self):
        return self.__pmall

    @property
    def nchoi1(self):
        return self.__nchoi1

    @property
    def nchoi(self):
        return self.__nchoi

    @property
    def nchoir(self):
        return self.__nchoir

    @property
    def nchoih(self):
        return self.__nchoih

    @property
    def nchtor(self):
        return self.__nchtor

    @property
    def nchbna(self):
        return self.__nchbna

    @property
    def nchbnb(self):
        return self.__nchbnb

    @property
    def icbdir(self):
        return self.__icbdir

    @property
    def icbsta(self):
        return self.__icbsta

    @property
    def rbsmax(self):
        return self.__rbsmax

    @property
    def rbsmin(self):
        return self.__rbsmin

    @property
    def avbmc_version(self):
        return self.__avbmc_version

    @property
    def pmbias(self):
        return self.__pmbias

    @property
    def pmbsmt(self):
        return self.__pmbsmt

    @property
    def pmbias2(self):
        return self.__pmbias2

    @rcutin.setter
    def rcutin(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "rcutin failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rcutin", False, repr(getattr(self, "rcutin")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rcutin", False, repr(getattr(self, "rcutin")), repr(val),
                    None
                )
            )
            self.__rcutin = val

    @pmcb.setter
    def pmcb(self,val):
        if not ti.is_probability(val):
            errorMessage = "pmcb failed test_instance.is_probability check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmcb", False, repr(getattr(self, "pmcb")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmcb", False, repr(getattr(self, "pmcb")), repr(val),
                    None
                )
            )
            self.__pmcb = val

    @pmcbmt.setter
    def pmcbmt(self, val):

        var = "pmcbmt"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmcbmt", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmcbmt", False, repr(getattr(self, "pmcbmt")), repr(val),
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
                        self.__location, "pmcbmt", False, repr(getattr(self, "pmcbmt")), repr(val),
                        None
                    )
                )
                self.__pmcbmt = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmcbmt", False, repr(getattr(self, "pmcbmt")), repr(val),
                    None
                )
            )
            self.__pmcbmt = val

    @pmall.setter
    def pmall(self, val):

        var = "pmall"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmall", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmall", False, repr(getattr(self, "pmall")), repr(val),
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
                        self.__location, "pmall", False, repr(getattr(self, "pmall")), repr(val),
                        None
                    )
                )
                self.__pmall = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmall", False, repr(getattr(self, "pmall")), repr(val),
                    None
                )
            )
            self.__pmall = val

    @nchoi1.setter
    def nchoi1(self, val):

        var = "nchoi1"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("nchoi1", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "nchoi1", False, repr(getattr(self, "nchoi1")), repr(val),
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
                        self.__location, "nchoi1", False, repr(getattr(self, "nchoi1")), repr(val),
                        None
                    )
                )
                self.__nchoi1 = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nchoi1", False, repr(getattr(self, "nchoi1")), repr(val),
                    None
                )
            )
            self.__nchoi1 = val

    @nchoi.setter
    def nchoi(self, val):

        var = "nchoi"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("nchoi", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "nchoi", False, repr(getattr(self, "nchoi")), repr(val),
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
                        self.__location, "nchoi", False, repr(getattr(self, "nchoi")), repr(val),
                        None
                    )
                )
                self.__nchoi = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nchoi", False, repr(getattr(self, "nchoi")), repr(val),
                    None
                )
            )
            self.__nchoi = val

    @nchoir.setter
    def nchoir(self, val):

        var = "nchoir"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("nchoir", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "nchoir", False, repr(getattr(self, "nchoir")), repr(val),
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
                        self.__location, "nchoir", False, repr(getattr(self, "nchoir")), repr(val),
                        None
                    )
                )
                self.__nchoir = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nchoir", False, repr(getattr(self, "nchoir")), repr(val),
                    None
                )
            )
            self.__nchoir = val

    @nchoih.setter
    def nchoih(self, val):

        var = "nchoih"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("nchoih", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "nchoih", False, repr(getattr(self, "nchoih")), repr(val),
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
                        self.__location, "nchoih", False, repr(getattr(self, "nchoih")), repr(val),
                        None
                    )
                )
                self.__nchoih = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nchoih", False, repr(getattr(self, "nchoih")), repr(val),
                    None
                )
            )
            self.__nchoih = val

    @nchtor.setter
    def nchtor(self, val):

        var = "nchtor"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("nchtor", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "nchtor", False, repr(getattr(self, "nchtor")), repr(val),
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
                        self.__location, "nchtor", False, repr(getattr(self, "nchtor")), repr(val),
                        None
                    )
                )
                self.__nchtor = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nchtor", False, repr(getattr(self, "nchtor")), repr(val),
                    None
                )
            )
            self.__nchtor = val

    @nchbna.setter
    def nchbna(self, val):

        var = "nchbna"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("nchbna", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "nchbna", False, repr(getattr(self, "nchbna")), repr(val),
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
                        self.__location, "nchbna", False, repr(getattr(self, "nchbna")), repr(val),
                        None
                    )
                )
                self.__nchbna = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nchbna", False, repr(getattr(self, "nchbna")), repr(val),
                    None
                )
            )
            self.__nchbna = val

    @nchbnb.setter
    def nchbnb(self, val):

        var = "nchbnb"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("nchbnb", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "nchbnb", False, repr(getattr(self, "nchbnb")), repr(val),
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
                        self.__location, "nchbnb", False, repr(getattr(self, "nchbnb")), repr(val),
                        None
                    )
                )
                self.__nchbnb = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nchbnb", False, repr(getattr(self, "nchbnb")), repr(val),
                    None
                )
            )
            self.__nchbnb = val

    @icbdir.setter
    def icbdir(self, val):

        var = "icbdir"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_integer(val)):
                errorMessage = logging.multidimensional_error("icbdir", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "icbdir", False, repr(getattr(self, "icbdir")), repr(val),
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
                        self.__location, "icbdir", False, repr(getattr(self, "icbdir")), repr(val),
                        None
                    )
                )
                self.__icbdir = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "icbdir", False, repr(getattr(self, "icbdir")), repr(val),
                    None
                )
            )
            self.__icbdir = val

    @icbsta.setter
    def icbsta(self, val):

        var = "icbsta"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_integer(val)):
                errorMessage = logging.multidimensional_error("icbsta", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "icbsta", False, repr(getattr(self, "icbsta")), repr(val),
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
                        self.__location, "icbsta", False, repr(getattr(self, "icbsta")), repr(val),
                        None
                    )
                )
                self.__icbsta = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "icbsta", False, repr(getattr(self, "icbsta")), repr(val),
                    None
                )
            )
            self.__icbsta = val

    @rbsmax.setter
    def rbsmax(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "rbsmax failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rbsmax", False, repr(getattr(self, "rbsmax")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rbsmax", False, repr(getattr(self, "rbsmax")), repr(val),
                    None
                )
            )
            self.__rbsmax = val

    @rbsmin.setter
    def rbsmin(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "rbsmin failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rbsmin", False, repr(getattr(self, "rbsmin")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rbsmin", False, repr(getattr(self, "rbsmin")), repr(val),
                    None
                )
            )
            self.__rbsmin = val

    @avbmc_version.setter
    def avbmc_version(self,val):
        if not ti.is_integer(val):
            errorMessage = "avbmc_version failed test_instance.is_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "avbmc_version", False, repr(getattr(self, "avbmc_version")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "avbmc_version", False, repr(getattr(self, "avbmc_version")), repr(val),
                    None
                )
            )
            self.__avbmc_version = val

    @pmbias.setter
    def pmbias(self, val):

        var = "pmbias"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmbias", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmbias", False, repr(getattr(self, "pmbias")), repr(val),
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
                        self.__location, "pmbias", False, repr(getattr(self, "pmbias")), repr(val),
                        None
                    )
                )
                self.__pmbias = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmbias", False, repr(getattr(self, "pmbias")), repr(val),
                    None
                )
            )
            self.__pmbias = val

    @pmbsmt.setter
    def pmbsmt(self, val):

        var = "pmbsmt"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmbsmt", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmbsmt", False, repr(getattr(self, "pmbsmt")), repr(val),
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
                        self.__location, "pmbsmt", False, repr(getattr(self, "pmbsmt")), repr(val),
                        None
                    )
                )
                self.__pmbsmt = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmbsmt", False, repr(getattr(self, "pmbsmt")), repr(val),
                    None
                )
            )
            self.__pmbsmt = val

    @pmbias2.setter
    def pmbias2(self, val):

        var = "pmbias2"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error("pmbias2", True)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "pmbias2", False, repr(getattr(self, "pmbias2")), repr(val),
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
                        self.__location, "pmbias2", False, repr(getattr(self, "pmbias2")), repr(val),
                        None
                    )
                )
                self.__pmbias2 = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "pmbias2", False, repr(getattr(self, "pmbias2")), repr(val),
                    None
                )
            )
            self.__pmbias2 = val

