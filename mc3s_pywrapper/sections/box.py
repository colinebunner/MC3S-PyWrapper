from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging

class Box:

    def __init__(
        self,boxlx=None,boxly=None,boxlz=None,rcut=None,kalp=None,
        rcutnn=None,numDimIso=None,lsolid=None,lrect=None,lideal=None,
        ltwice=None,T=None,P=None,ininch=None,ghost_particles=None,inix=None,
        iniy=None,iniz=None,inirot=None,inimix=None,zshift=None,dshift=None,
        use_linkcell=None,rintramax=None,errorLog=[],changeLog=[],location=""
    ):

        self.__boxlx = boxlx
        self.__boxly = boxly
        self.__boxlz = boxlz
        self.__rcut = rcut
        self.__kalp = kalp
        self.__rcutnn = rcutnn
        self.__numDimIso = numDimIso
        self.__lsolid = lsolid
        self.__lrect = lrect
        self.__lideal = lideal
        self.__ltwice = ltwice
        self.__T = T
        self.__P = P
        self.__ininch = ininch
        self.__ghost_particles = ghost_particles
        self.__inix = inix
        self.__iniy = iniy
        self.__iniz = iniz
        self.__inirot = inirot
        self.__inimix = inimix
        self.__zshift = zshift
        self.__dshift = dshift
        self.__use_linkcell = use_linkcell
        self.__rintramax = rintramax
        self.__errorLog = errorLog
        self.__changeLog = changeLog
        self.__location = "{}/Box".format(location)


    @property
    def boxlx(self):
        return self.__boxlx

    @property
    def boxly(self):
        return self.__boxly

    @property
    def boxlz(self):
        return self.__boxlz

    @property
    def rcut(self):
        return self.__rcut

    @property
    def kalp(self):
        return self.__kalp

    @property
    def rcutnn(self):
        return self.__rcutnn

    @property
    def numDimIso(self):
        return self.__numDimIso

    @property
    def lsolid(self):
        return self.__lsolid

    @property
    def lrect(self):
        return self.__lrect

    @property
    def lideal(self):
        return self.__lideal

    @property
    def ltwice(self):
        return self.__ltwice

    @property
    def T(self):
        return self.__T

    @property
    def P(self):
        return self.__P

    @property
    def ininch(self):
        return self.__ininch

    @property
    def ghost_particles(self):
        return self.__ghost_particles

    @property
    def inix(self):
        return self.__inix

    @property
    def iniy(self):
        return self.__iniy

    @property
    def iniz(self):
        return self.__iniz

    @property
    def inirot(self):
        return self.__inirot

    @property
    def inimix(self):
        return self.__inimix

    @property
    def zshift(self):
        return self.__zshift

    @property
    def dshift(self):
        return self.__dshift

    @property
    def use_linkcell(self):
        return self.__use_linkcell

    @property
    def rintramax(self):
        return self.__rintramax

    @boxlx.setter
    def boxlx(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "boxlx failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "boxlx", False, repr(getattr(self, "boxlx")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "boxlx", False, repr(getattr(self, "boxlx")), repr(val),
                    None
                )
            )
            self.__boxlx = val

    @boxly.setter
    def boxly(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "boxly failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "boxly", False, repr(getattr(self, "boxly")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "boxly", False, repr(getattr(self, "boxly")), repr(val),
                    None
                )
            )
            self.__boxly = val

    @boxlz.setter
    def boxlz(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "boxlz failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "boxlz", False, repr(getattr(self, "boxlz")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "boxlz", False, repr(getattr(self, "boxlz")), repr(val),
                    None
                )
            )
            self.__boxlz = val

    @rcut.setter
    def rcut(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "rcut failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rcut", False, repr(getattr(self, "rcut")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rcut", False, repr(getattr(self, "rcut")), repr(val),
                    None
                )
            )
            self.__rcut = val

    @kalp.setter
    def kalp(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "kalp failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "kalp", False, repr(getattr(self, "kalp")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "kalp", False, repr(getattr(self, "kalp")), repr(val),
                    None
                )
            )
            self.__kalp = val

    @rcutnn.setter
    def rcutnn(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "rcutnn failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rcutnn", False, repr(getattr(self, "rcutnn")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rcutnn", False, repr(getattr(self, "rcutnn")), repr(val),
                    None
                )
            )
            self.__rcutnn = val

    @numDimIso.setter
    def numDimIso(self,val):
        if not ti.is_integer(val):
            errorMessage = "numDimIso failed test_instance.is_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "numDimIso", False, repr(getattr(self, "numDimIso")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "numDimIso", False, repr(getattr(self, "numDimIso")), repr(val),
                    None
                )
            )
            self.__numDimIso = val

    @lsolid.setter
    def lsolid(self,val):
        if not ti.is_boolean(val):
            errorMessage = "lsolid failed test_instance.is_boolean check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lsolid", False, repr(getattr(self, "lsolid")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lsolid", False, repr(getattr(self, "lsolid")), repr(val),
                    None
                )
            )
            self.__lsolid = val

    @lrect.setter
    def lrect(self,val):
        if not ti.is_boolean(val):
            errorMessage = "lrect failed test_instance.is_boolean check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lrect", False, repr(getattr(self, "lrect")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lrect", False, repr(getattr(self, "lrect")), repr(val),
                    None
                )
            )
            self.__lrect = val

    @lideal.setter
    def lideal(self,val):
        if not ti.is_boolean(val):
            errorMessage = "lideal failed test_instance.is_boolean check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lideal", False, repr(getattr(self, "lideal")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "lideal", False, repr(getattr(self, "lideal")), repr(val),
                    None
                )
            )
            self.__lideal = val

    @ltwice.setter
    def ltwice(self,val):
        if not ti.is_boolean(val):
            errorMessage = "ltwice failed test_instance.is_boolean check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ltwice", False, repr(getattr(self, "ltwice")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ltwice", False, repr(getattr(self, "ltwice")), repr(val),
                    None
                )
            )
            self.__ltwice = val

    @T.setter
    def T(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "T failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "T", False, repr(getattr(self, "T")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "T", False, repr(getattr(self, "T")), repr(val),
                    None
                )
            )
            self.__T = val

    @P.setter
    def P(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "P failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "P", False, repr(getattr(self, "P")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "P", False, repr(getattr(self, "P")), repr(val),
                    None
                )
            )
            self.__P = val

    @ininch.setter
    def ininch(self, val):

        var = "ininch"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("ininch", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "ininch", False, repr(getattr(self, "ininch")), repr(val),
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
                        self.__location, "ininch", False, repr(getattr(self, "ininch")), repr(val),
                        None
                    )
                )
                self.__ininch = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ininch", False, repr(getattr(self, "ininch")), repr(val),
                    None
                )
            )
            self.__ininch = val

    @ghost_particles.setter
    def ghost_particles(self, val):

        var = "ghost_particles"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_positive_integer(val)):
                errorMessage = logging.multidimensional_error("ghost_particles", False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, "ghost_particles", False, repr(getattr(self, "ghost_particles")), repr(val),
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
                        self.__location, "ghost_particles", False, repr(getattr(self, "ghost_particles")), repr(val),
                        None
                    )
                )
                self.__ghost_particles = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "ghost_particles", False, repr(getattr(self, "ghost_particles")), repr(val),
                    None
                )
            )
            self.__ghost_particles = val

    @inix.setter
    def inix(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "inix failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "inix", False, repr(getattr(self, "inix")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "inix", False, repr(getattr(self, "inix")), repr(val),
                    None
                )
            )
            self.__inix = val

    @iniy.setter
    def iniy(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "iniy failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "iniy", False, repr(getattr(self, "iniy")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "iniy", False, repr(getattr(self, "iniy")), repr(val),
                    None
                )
            )
            self.__iniy = val

    @iniz.setter
    def iniz(self,val):
        if not ti.is_positive_integer(val):
            errorMessage = "iniz failed test_instance.is_positive_integer check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "iniz", False, repr(getattr(self, "iniz")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "iniz", False, repr(getattr(self, "iniz")), repr(val),
                    None
                )
            )
            self.__iniz = val

    @inirot.setter
    def inirot(self,val):
        if not ti.is_number(val):
            errorMessage = "inirot failed test_instance.is_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "inirot", False, repr(getattr(self, "inirot")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "inirot", False, repr(getattr(self, "inirot")), repr(val),
                    None
                )
            )
            self.__inirot = val

    @inimix.setter
    def inimix(self,val):
        if not ti.is_number(val):
            errorMessage = "inimix failed test_instance.is_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "inimix", False, repr(getattr(self, "inimix")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "inimix", False, repr(getattr(self, "inimix")), repr(val),
                    None
                )
            )
            self.__inimix = val

    @zshift.setter
    def zshift(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "zshift failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "zshift", False, repr(getattr(self, "zshift")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "zshift", False, repr(getattr(self, "zshift")), repr(val),
                    None
                )
            )
            self.__zshift = val

    @dshift.setter
    def dshift(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "dshift failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "dshift", False, repr(getattr(self, "dshift")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "dshift", False, repr(getattr(self, "dshift")), repr(val),
                    None
                )
            )
            self.__dshift = val

    @use_linkcell.setter
    def use_linkcell(self,val):
        if not ti.is_boolean(val):
            errorMessage = "use_linkcell failed test_instance.is_boolean check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "use_linkcell", False, repr(getattr(self, "use_linkcell")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "use_linkcell", False, repr(getattr(self, "use_linkcell")), repr(val),
                    None
                )
            )
            self.__use_linkcell = val

    @rintramax.setter
    def rintramax(self,val):
        if not ti.is_positive_number(val):
            errorMessage = "rintramax failed test_instance.is_positive_number check."
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rintramax", False, repr(getattr(self, "rintramax")), repr(val),
                     errorMessage
               )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "rintramax", False, repr(getattr(self, "rintramax")), repr(val),
                    None
                )
            )
            self.__rintramax = val

