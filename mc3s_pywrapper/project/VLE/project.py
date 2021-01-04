# A Signac-Flow project for one-component VLE simulations, a standard simulation in the Siepmann group
import json
import os
import pickle
import shutil
import subprocess
import numpy as np

import signac
from flow import FlowProject, directive

# Melt, cool, volume, swap
equilibrate = FlowProject.make_group(name="equilibrate")

project = signac.get_project()

@FlowProject.label
def is_equil(job):
    """
        For job tasks in the 'equilibrate' group, we only
        want to run the task if it 
    """

    return job.sp.run == "equil"

@FlowProject.label
def job_marked_complete(job):
    """
        For jobs that may have multiple steps, mark completion
        in the job database
    """
    return getattr(j.data, "complete", False)

@equilibrate
@FlowProject.operation
@FlowProject.pre(is_equil)
@FlowProject.post.isfile("melt.run1a.dat")
def melt(job):

    # Open up pickle Sim object
    with open(job.sp.simPath, "rb") as f:
        mySim = pickle.load(f)

    # Make sure linit is True
    if not mySim.shared.linit:
        mySim.shared.linit = True

    # The way I'm setting up electrostatics in this simulation
    # I want LEwaldAuto
    if not mySim.system.L_Ewald_Auto:
        mySim.system.L_Ewald_Auto = True

    # Set the desired number of cycles
    ncyc = 2000
    mySim.shared.nstep  = ncyc

    # Set iratio such that it isn't adjusted during this step
    mySim.shared.iratio = ncyc + 1

    # Set printing level for this step
    mySim.analysis.iprint = int(ncyc//5)
    mySim.analysis.imv = ncyc+1
    mySim.analysis.iblock = int(ncyc//5)
    mySim.analysis.iratp = ncyc+1
    # Never call these
    mySim.analysis.idiele = 1000000
    mySim.analysis.iheatcapacity = 1000000
    mySim.analysis.ianalyze = 1000000

    # Don't adjust volume
    mySim.pmvol = 0.0e0
    mySim.volume.iratv = ncyc+1

    # Make sure we don't swatch
    mySim.swatch.pmswat = 0.0e0

    # Make sure no swapping right now
    mySim.swap.pmswap = 0.0e0

    # Adjust CBMC (will search for better parameters later)
    #mySim.cbmc.rcutin = 6.0
    mySim.cbmc.pmcb = 0.0e0
    
    # Setting translation probability to 50% of moves
    # NOTE: Need to make this more intelligent for molecules with reduced D.O.F. (i.e. single-site LJ)
    mySim.simple.pmtra = 0.5

    # Make sure flucq is off for this model (if you're doing polarizable, obv need to adjust this workflow)
    mySim.flucq.pmflcq = 0.0e0

    # Set up boxes (labels are 1 & 2, 1 will be liquid and 2 vapor in this workflow)
    for box_num in [1, 2]:
        box = mySim.boxes[box_num]
        # Set temperature to 10x job temperature for melt stage
        box.T = 10*job.sp.T

        # Setup boxes based on density guesses, using best practices for
        # partitioning molecules between vapor and liquid phases
        if box_num == 1:
            dg    = job.data.vapor_density_guess
            ninit = int(0.15*mySim.shared.nchain)
        else:
            dg = job.data.liquid_density_guess
            ninit = mySim.shared.nchain - int(0.15*mySim.shared.nchain)

        # Conversion factor for going from mol/L to chain/A^3
        cfac = 0.0006022

        min_cube = int(np.cbrt(ninit)) + 1
        bl = np.round(np.cbrt(ninit/(dg*cfac)), decimals=2)

        box.numDimIso = 3
        box.nchain_mt = [ninit]
        box.ghost_particles = 0
        box.inix = min_cube
        box.iniy = min_cube
        box.iniz = min_cube
        box.boxlx = bl
        box.boxly = bl
        box.boxlz = bl
        box.inirot = 0
        box.inimix = 1
        box.zshift = 0.0e0
        box.dshift = np.round(bl/min_cube, decimals=2)

        if box_num == 1:
            box.rcut = 14.0
        else:
            box.rcut = 0.4*bl

    # Write fort.4 and topmon.inp files to this job workdir
    mySim.io.file_input = "fort.4"
    mySim.write_fort4()
    mySim.write_topmon()

    # Run the job
    start, end, success, msg = mySim.run_mc3s()

    # Point to the restart file
    mySim.io.file_restart = os.path.join(
        job.ws, "melt.config1a.dat"
    )

    # Log our simulation
    mySim.logJob(
        start, end, job.ws, success, msg, "melt", copy=True
    )

    # Dump our simulation object in the project directory for later loading
    job.data.simPath = os.path.join(project.root_directory(), f"{job.id}.pkl")
    with open(job.data.simPath, "wb") as f:
        pickle.dump(mySim, f, protocol=pickle.HIGHEST_PROTOCOL)

@equilibrate
@FlowProject.operation
@FlowProject.pre(is_equil)
@FlowProject.pre.after(melt)
@FlowProject.post.isfile("cool.run1a.dat")
def cool(job):

    # Open up pickle Sim object
    with open(job.data.simPath, "rb") as f:
        mySim = pickle.load(f)

    # Set linit to False
    mySim.shared.linit = False

    # Set the desired number of cycles
    ncyc = 5000
    mySim.shared.nstep  = ncyc

    # Set iratio such that it isn't adjusted during this step
    mySim.shared.iratio = ncyc + 1

    # Set printing level for this step
    mySim.analysis.iprint = int(ncyc//5)
    mySim.analysis.imv = ncyc+1
    mySim.analysis.iblock = int(ncyc//5)
    mySim.analysis.iratp = ncyc+1

    # Fix the temperature
    for box_num in range(1,3):
        mySim.boxes[box_num].T = job.sp.T

    # Write fort.4 and topmon.inp files to this job workdir
    # NOTE: file_input is fort.4 (not an abspath), so no need to change
    mySim.write_fort4()
    mySim.write_topmon()

    # Run the job
    start, end, success, msg = mySim.run_mc3s()

    # Point to the restart file
    mySim.io.file_restart = os.path.join(
        job.ws, "cool.config1a.dat"
    )

    # Log our simulation
    mySim.logJob(
        start, end, job.ws, success, msg, "cool", copy=True
    )

    # Dump our simulation object in the project directory for later loading
    with open(job.data.simPath, "wb") as f:
        pickle.dump(mySim, f, protocol=pickle.HIGHEST_PROTOCOL)

@equilibrate
@FlowProject.operation
@FlowProject.pre(is_equil)
@FlowProject.pre.after(cool)
@FlowProject.post.isfile("volume.run1a.dat")
def volume(job):

    # Open up pickle Sim object
    with open(job.data.simPath, "rb") as f:
        mySim = pickle.load(f)

    # Set linit to False
    mySim.shared.linit = False

    # Set the desired number of cycles
    ncyc = 10000
    mySim.shared.nstep  = ncyc

    # Set iratio such that it isn't adjusted during this step
    mySim.shared.iratio = ncyc + 1

    # Set printing level for this step
    mySim.analysis.iprint = int(ncyc//5)
    mySim.analysis.imv = ncyc+1
    mySim.analysis.iblock = int(ncyc//5)
    mySim.analysis.iratp = ncyc+1

    # Adjust move probabilities now that volume needs to be active
    mySim.volume.pmvol = 1./(mySim.volume.tavol*mySim.share.nchain)
    mySim.simple.pmtra = (1 - mySim.volume.pmvol)/2. + mySim.volume.pmvol

    # Write fort.4 and topmon.inp files to this job workdir
    mySim.write_fort4()
    mySim.write_topmon()

    # Point to the restart file
    mySim.io.file_restart = os.path.join(
        job.ws, "volume.config1a.dat"
    )

    # Log our simulation
    mySim.logJob(
        start, end, job.ws, success, msg, "volume", copy=True
    )

    # Dump our simulation object in the project directory for later loading
    with open(job.data.simPath, "wb") as f:
        pickle.dump(mySim, f, protocol=pickle.HIGHEST_PROTOCOL)

@equilibrate
@FlowProject.operation
@FlowProject.pre(is_equil)
@FlowProject.pre.after(volume)
@FlowProject.post(job_marked_complete)
def swap(job):

    # Open up pickle Sim object
    with open(job.data.simPath, "rb") as f:
        mySim = pickle.load(f)

    # Set linit to False
    mySim.shared.linit = False

    # Set the desired number of cycles
    ncyc = 10000
    mySim.shared.nstep  = ncyc

    # Set iratio such that it isn't adjusted during this step
    mySim.shared.iratio = ncyc + 1

    # Set printing level for this step
    mySim.analysis.iprint = int(ncyc//5)
    mySim.analysis.imv = ncyc+1
    mySim.analysis.iblock = int(ncyc//5)
    mySim.analysis.iratp = ncyc+1

    # Adjust move probabilities now that volume needs to be active
    mySim.volume.pmvol = 1./(mySim.volume.tavol*mySim.share.nchain)
    mySim.simple.pmtra = (1 - mySim.volume.pmvol)/2. + mySim.volume.pmvol

    # Write fort.4 and topmon.inp files to this job workdir
    mySim.write_fort4()
    mySim.write_topmon()

    # Point to the restart file
    mySim.io.file_restart = os.path.join(
        job.ws, "volume.config1a.dat"
    )

    # Log our simulation
    mySim.logJob(
        start, end, job.ws, success, msg, "volume", copy=True
    )

    # Dump our simulation object in the project directory for later loading
    with open(job.data.simPath, "wb") as f:
        pickle.dump(mySim, f, protocol=pickle.HIGHEST_PROTOCOL)