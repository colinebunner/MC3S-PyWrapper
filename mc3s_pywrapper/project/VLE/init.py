import signac
import pickle

from mc3s_pywrapper.mc_sim import Sim

project = signac.init_project('VLE')

# Path to your topmon.inp and fort.4, if you haven't moved them into the
# signac directory
top = "topmon.inp"
f4  = "fort.4"

# Path to your working MCCCS-MN executable
execPath = "/home/siepmann/bunne043/MCCCS-MN/exe-mesabi/src"

Ts = [297, 350, 400, 450, 500, 550]
# Guesses for the density in mol/L
# Experimental values from NIST fluid properties database
vapor_density_guess = {
    297: 0.0012002,
    350: 0.014448,
    400: 0.076014,
    450: 0.26711,
    500: 0.73265,
    550: 1.7471
}
liquid_density_guess = {
    297: 55.358,
    350: 54.049,
    400: 52.038,
    450: 49.421,
    500: 46.145,
    550: 41.954
}
num_runs = 10
runs = list(range(num_runs)) + ["equil"]

mySim   = Sim.from_inputs(top, f4, name="VLE")
simPath = os.path.abspath("mc_sim.pkl")
with open(simPath, "wb") as f:
    pickle.dump(mySim, f)

for run in runs:
    for T in Ts:
        sp = {"T": T, "run": run}
        job = project.open_job(sp)
        job.init()
        job.data.vapor_density_guess = vapor_density_guess[T]
        job.data.liquid_density_guess = liquid_density_guess[T]
        job.data.simPath = simPath