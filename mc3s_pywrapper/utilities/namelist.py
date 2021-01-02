namelists = {
    "simple":
        [
            {"name": "pm_atom_tra", "type": "probability"},
            {"name": "Armtra", "type": "oda", "oda_type": "positive_number"},
            {"name": "pmtra", "type": "probability"},
            {"name": "pmtrmt", "type": "oda", "oda_type": "probability"},
            {"name": "rmtra", "type": "oda", "oda_type": "positive_number"},
            {"name": "tatra", "type": "probability"},
            {"name": "pmromt", "type": "oda", "oda_type": "probability"},
            {"name": "rmrot", "type": "oda", "oda_type": "positive_number"},
            {"name": "tarot", "type": "probability"}
        ],
    "external_field":
        [
            {"name": "Elect_field", "type": "number"}
        ],
    "swatch":
        [
            {"name": "pmswat", "type": "probability"},
            {"name": "nswaty", "type": "positive_int"},
            {"name": "pmsatc", "type": "oda", "oda_type": "probability"}
        ],
    "flucq":
        [
            {"name": "taflcq", "type": "probability"},
            {"name": "fqtemp", "type": "number"},
            {"name": "rmflucq", "type": "positive_number"},
            {"name": "pmflcq", "type": "probability"},
            {"name": "pmfqmt", "type": "oda", "oda_type": "probability"},
            {"name": "lflucq", "type": "oda", "oda_type": "boolean"},
            {"name": "lqtrans", "type": "oda", "oda_type": "boolean"},
            {"name": "fqegp", "type": "oda", "oda_type": "number"},
            {"name": "nchoiq", "type": "oda", "oda_type": "positive_int"},
            {"name": "nswapq", "type": "positive_int"}
        ],
    "gcmc":
        [
            {"name": "nequil", "type": "positive_int"},
            {"name": "ninstf", "type": "positive_int"},
            {"name": "ninsth", "type": "positive_int"},
            {"name": "ndumph", "type": "positive_int"},
            {"name": "B", "type": "oda", "oda_type": "number"}
        ],
    "ee":
        [
            {"name": "pmexpc", "type": "probability"},
            {"name": "pmeemt", "type": "oda", "oda_type": "probability"},
            {"name": "pmexpc1", "type": "probability"},
            {"name": "lexpand", "type": "oda", "oda_type": "boolean"}
        ],
    "box":
        [
            {"name": "boxlx", "type": "positive_number"},
            {"name": "boxly", "type": "positive_number"},
            {"name": "boxlz", "type": "positive_number"},
            {"name": "rcut", "type": "positive_number"},
            {"name": "kalp", "type": "positive_number"},
            {"name": "rcutnn", "type": "positive_number"},
            {"name": "numDimIso", "type": "int"},
            {"name": "lsolid", "type": "boolean"},
            {"name": "lrect", "type": "boolean"},
            {"name": "lideal", "type": "boolean"},
            {"name": "ltwice", "type": "boolean"},
            {"name": "T", "type": "positive_number"},
            {"name": "P", "type": "positive_number"},
            {"name": "ininch", "type": "oda", "oda_type": "positive_int"},
            {"name": "ghost_particles", "type": "oda", "oda_type": "positive_int"},
            {"name": "inix", "type": "positive_int"},
            {"name": "iniy", "type": "positive_int"},  
            {"name": "iniz", "type": "positive_int"},  
            {"name": "inirot", "type": "number"},
            {"name": "inimix", "type": "number"},
            {"name": "zshift", "type": "positive_number"},
            {"name": "dshift", "type": "positive_number"},
            {"name": "use_linkcell", "type": "boolean"},
            {"name": "rintramax", "type": "positive_number"}
        ]
}

# What is this? Well, I thought it would be clever to combine some sections of the input files
# together or make the names shorter. So now, when I want to read input files and write the 
# data to one of my Sim objects, I have to use this map from the raw input to the write object 
# attribute. I got what was coming to me, I guess.
n2p = {
    "mc_shared": "shared",
    "analysis": "analysis",
    "external_field": "external_field",
    "mc_volume": "volume",
    "mc_swatch": "swatch",
    "mc_cbmc": "cbmc",
    "mc_flucq": "flucq",
    "mc_gcmc": "gcmc",
    "mc_ee": "ee",
    "mc_simple": "simple",
    "io": "io",
    "system": "system"
}

p2n = {val: key for key, val in n2p.items()}