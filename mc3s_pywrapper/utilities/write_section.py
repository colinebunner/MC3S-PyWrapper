from mc3s_pywrapper.utilities import test_instance as ti
from mc3s_pywrapper.utilities import oneDimArray   as oda
from mc3s_pywrapper.utilities import logging
from mc3s_pywrapper.utilities.namelist import p2n

def write_section(name, variables):

    '''
        Setting up the modules is a pain by hand since I am type-checking. This is
        a script to take an easier to assemble set of information and write all
        the boiler plate. It assembles the getters/setters. The __init__ is filled
        out, but there are possibly many situations in which you would want to edit
        this.
    '''

    # Generate setter for oneDimArrays
    def oda_setter_template(var_name, probability, ti_func):
        # Yes, I use spaces not tabs
        return (
            f"    @{var_name}.setter\n"
            f"    def {var_name}(self, val):\n\n"
            f"        var = \"{var_name}\"\n\n"
            f"        if not isinstance(val, oda.oneDimArray):\n"
            f"            if not (isinstance(val, list) or ti.{ti_func}(val)):\n"
            f"                errorMessage = logging.multidimensional_error(\"{var_name}\", {probability})\n"
            "                self.__changeLog.append(\n"
            "                    logging.changelog_entry(\n"
            f"                        self.__location, \"{var_name}\", False, repr(getattr(self, \"{var_name}\")), repr(val),\n"
            "                        errorMessage\n"
            "                    )\n"
            "                )\n"
            "                self.__errorLog.append(\n"
            "                    logging.errorlog_entry(\"Setter\", errorMessage)\n"
            "                )\n"
            "            else:\n"
            "                if not isinstance(val,list):\n"
            "                    val = [val]\n"
            "                myODA = oda.oneDimArray.listToODA(val,errorLog=self.__errorLog,changeLog=self.__changeLog,\n"
            "                                location=self.__location,var=var)\n"
            "                self.__changeLog.append(\n"
            "                    logging.changelog_entry(\n"
            f"                        self.__location, \"{var_name}\", False, repr(getattr(self, \"{var_name}\")), repr(val),\n"
            "                        None\n"
            "                    )\n"
            "                )\n"
            f"                self.__{var_name} = myODA\n"
            "        else:\n"
            "            self.__changeLog.append(\n"
            "                logging.changelog_entry(\n"
            f"                    self.__location, \"{var_name}\", False, repr(getattr(self, \"{var_name}\")), repr(val),\n"
            "                    None\n"
            "                )\n"
            "            )\n"
            f"            self.__{var_name} = val\n\n"
        )

    def value_setter_template(var_name, ti_func):
        return (
            f"    @{var_name}.setter\n"
            f"    def {var_name}(self,val):\n"
            f"        if not ti.{ti_func}(val):\n"
            f"            errorMessage = \"{var_name} failed test_instance.{ti_func} check.\"\n"
            "            self.__changeLog.append(\n"
            "                logging.changelog_entry(\n"
            f"                    self.__location, \"{var_name}\", False, repr(getattr(self, \"{var_name}\")), repr(val),\n"
            "                     errorMessage\n"
            "               )\n"
            "            )\n"
            "            self.__errorLog.append(\n"
            "                logging.errorlog_entry(\"Setter\", errorMessage)\n"
            "            )\n"
            "        else:\n"
            "            self.__changeLog.append(\n"
            "                logging.changelog_entry(\n"
            f"                    self.__location, \"{var_name}\", False, repr(getattr(self, \"{var_name}\")), repr(val),\n"
            "                    None\n"
            "                )\n"
            "            )\n"
            f"            self.__{var_name} = val\n\n"
        )
    
    type_2_ti = {
        "number": "is_number",
        "positive_number": "is_positive_number",
        "int": "is_integer",
        "positive_int": "is_positive_integer",
        "probability": "is_probability",
        "boolean": "is_boolean"
    }

    # Writing the code with good, old-fashioned string operations
    init_string = ""    
    init_set = ""
    for i, v in enumerate(variables):
        nm = v["name"]
        if i == 0:
            init_string += f"{nm}=None"
        elif i%2 == 0:
            init_string += f",{nm}=None\n"
        else:
            init_string += f",{nm}=None"

        init_set += f"        self.__{nm} = {nm}\n"

    code = (
        "from mc3s_pywrapper.utilities import test_instance as ti\n"
        "from mc3s_pywrapper.utilities import oneDimArray   as oda\n"
        "from mc3s_pywrapper.utilities import logging\n\n"
        f"class {name.capitalize()}:\n\n"
        "    def __init__(\n"
        "        self," + init_string +
        "        errorLog=[],changeLog=[],location=\"\"\n"
        "    ):\n\n" +
        init_set +
        f"        self.__errorLog = errorLog\n"
        f"        self.__changeLog = changeLog\n"
        f"        self.__location = \"{'{}'}/{name}\".format(location)\n\n\n"
    )

    properties = ""
    setters = ""

    for var in variables:
        name     = var["name"]
        var_type = var["type"]

        properties += f"    @property\n    def {name}(self):\n        return self.__{name}\n\n"

        # oneDimArrays are a little trickier
        if var_type == "oda":
            var_type = var["oda_type"]
            probability = var_type in ["probability"]
            setters += oda_setter_template(name, probability, type_2_ti[var_type])
        else:
            setters += value_setter_template(name, type_2_ti[var_type])

    return code + properties + setters

def write_fort4_code(name, variables):

    '''
        replaceme is so I can change to newlines (otherwise the file write would just expand
        that newline).
    '''

    namelist_name = p2n[name]

    writer_code = f"  fort4 += \"&{namelist_name}\"\n"

    newline = "\n"

    for v in variables:
        nm = v["name"]
        vtype = v["type"]

        # Need to call unrolledString method
        if vtype == "oda":
            writer_code += (
                f"  if simObj.{name}.{nm} is not None:\n"
                f"    fort4 += \"  = {{}}replaceme\".format(simObj.{name}.{nm}.unrolledString())\n"
            )
        else:
            writer_code += (
                f"  if simObj.{name}.{nm} is not None:\n"
                f"    fort4 += \"  = {{}}replaceme\".format(simObj.{name}.{nm})\n"
            )
    writer_code += (
        f"  fort4 += f\"/ replacemereplaceme\""
    )

    return writer_code