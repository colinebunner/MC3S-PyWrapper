import datetime
from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import objectArray as oba
from mc3s_pywrapper.utilities import logging

class SwapTable:

    '''
        This corresponds to the fort.4 section MC_SWAP, NOT the namelist mc_swap.
    '''    

    def __init__(
        self,number=None,nswapb=None,pmswapb=None,boxPairs=None,errorLog=[],changeLog=[],location=""
    ):
        self.__number    = number
        self.__nswapb    = nswapb
        self.__pmswapb   = pmswapb
        self.__boxPairs  = boxPairs
        self.__errorLog  = errorLog
        self.__changeLog = changeLog
        self.__location  = "{}/SwapTable-{}".format(location,number)

    @property
    def number(self):
        return self.__number

    @property
    def nswapb(self):
        return self.__nswapb
    
    @property
    def pmswapb(self):
        return self.__pmswapb
    
    @property
    def boxPairs(self):
        return self.__boxPairs

    @nswapb.setter
    def nswapb(self, val):
        if not ti.is_positive_integer(val):
            errorMessage = "nswapb must be a positive integer"
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nswapb", False, repr(getattr(self, "nswapb")), repr(val),
                    errorMessage
                )
            )
            self.__errorLog.append(
                logging.errorlog_entry("Setter", errorMessage)
            )
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, "nswapb", False, repr(getattr(self, "nswapb")), repr(val),
                    None
                )
            )
            self.__nswapb = val

    @pmswapb.setter
    def pmswapb(self, val):

        var = "pmswapb"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error(var, False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, var, False, repr(getattr(self, var)), repr(val),
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
                        self.__location, var, True, repr(getattr(self, var)), repr(val),
                        None
                    )
                )
                self.__pmswapb = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, var, True, repr(getattr(self, var)), repr(val),
                    None
                )
            )
            self.__pmswapb = val

    @boxPairs.setter
    def boxPairs(self, val):
        
        var = "boxPairs"

        if not isinstance(val, oda.oneDimArray):
            if not (isinstance(val, list) or ti.is_probability(val)):
                errorMessage = logging.multidimensional_error(var, False)
                self.__changeLog.append(
                    logging.changelog_entry(
                        self.__location, var, False, repr(getattr(self, var)), repr(val),
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
                        self.__location, var, True, repr(getattr(self, var)), repr(val),
                        None
                    )
                )
                self.__boxPairs = myODA
        else:
            self.__changeLog.append(
                logging.changelog_entry(
                    self.__location, var, True, repr(getattr(self, var)), repr(val),
                    None
                )
            )
            self.__boxPairs = val