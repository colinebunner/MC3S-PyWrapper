# What is this? Well, I thought it would be clever to combine some sections of the input files
# together or make the names shorter. So now, when I want to read input files and write the 
# data to one of my Sim objects, I have to use this map from the raw input to the write object 
# attribute. I got what was coming to me, I guess.
#
# Technical note: None is for unsupported fields. These fields will be added eventually,
# just gotta triage the work.
n2p = {
    "mc_shared": "shared",
    "analysis": "analysis",
    "external_field": None,
    "mc_volume": "volume",
    "mc_swatch": None,
    "mc_cbmc": "cbmc",
    "mc_flucq": None,
    "mc_gcmc": None,
    "mc_ee": None,
    "mc_simple": "simple"
}