import datetime

class IO:

  def __init__(self,file_input="fort.4",file_restart="fort.77",file_struct="input_struct.xyz",file_run="run1a.dat",
                    file_movie="movie1a.dat",file_solute="solute.dat",file_traj="fort.12",outputLocation="file",
                    run_num=1,suffix="a",L_movie_xyz=None,L_movie_pdb=None,file_cbmc_bend="cbmc_bend_table.dat",
                    checkpoint_interval=None,checkpoint_copies=None,use_checkpoint=None,ltraj=None,changeLog=[],
                    errorLog=[]):

    self.__file_input          = file_input
    self.__file_restart        = file_restart
    self.__file_struct         = file_struct
    self.__file_run            = file_run
    self.__file_movie          = file_movie
    self.__file_solute         = file_solute
    self.__file_traj           = file_traj
    self.__outputLocation      = outputLocation
    self.__run_num             = run_num
    self.__suffix              = suffix
    self.__L_movie_xyz         = L_movie_xyz
    self.__L_movie_pdb         = L_movie_pdb
    self.__file_cbmc_bend      = file_cbmc_bend
    self.__ltraj               = ltraj
    self.__changeLog           = changeLog
    self.__errorLog            = errorLog
    if (outputLocation.upper()=="FILE"):  # Rather have users choose "screen" or "terminal" than 2 or 6 
                                          # like original MCCCS input
      self.__io_output = 2
    elif (outputLocation.upper()=="TERMINAL"):
      self.__io_output = 6
    else:
      errorMessage = ("Couldn't set code output location {}. Options are \"file\" or "
                      "\"terminal\" (any case).".format(outputLocation))
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'__init__','Module':'IO',
                              'Variable':'outputLocation','ErrorMessage':errorMessage})


  @property
  def file_input(self):
    return self.__file_input

  @property
  def file_restart(self):
    return self.__file_restart

  @property
  def file_struct(self):
    return self.__file_struct

  @property
  def file_run(self):
    return self.__file_run

  @property
  def file_movie(self):
    return self.__file_movie

  @property
  def file_solute(self):
    return self.__file_solute

  @property
  def file_traj(self):
    return self.__file_traj

  @property
  def outputLocation(self):
    return self.__outputLocation

  @property
  def io_output(self):
    return self.__io_output

  @property
  def run_num(self):
    return self.__run_num

  @property
  def suffix(self):
    return self.__suffix

  @property
  def L_movie_xyz(self):
    return self.__L_movie_xyz

  @property
  def L_movie_pdb(self):
    return self.__L_movie_pdb

  @property
  def file_cbmc_bend(self):
    return self.__L_movie_pdb

  @property
  def checkpoint_interval(self):
    return self.__checkpoint_interval

  @property
  def checkpoint_copies(self):
    return self.__checkpoint_copies

  @property
  def use_checkpoint(self):
    return self.__use_checkpoint

  @property
  def ltraj(self):
    return self.__ltraj

  @file_input.setter
  def file_input(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'fileInput',
                             'Success':True,'Previous':self.__file_input,'New':val,'ErrorMessage':None})
    self.__file_input = str(val)

  @file_restart.setter
  def file_restart(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'file_restart',
                             'Success':True,'Previous':self.__file_restart,'New':val,
                             'ErrorMessage':None})
    self.__file_restart = str(val)

  @file_struct.setter
  def file_struct(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'file_struct',
                             'Success':True,'Previous':self.__file_struct,'New':val,'ErrorMessage':None})
    self.__file_struct = str(val)

  @file_run.setter
  def file_run(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'file_run',
                             'Success':True,'Previous':self.__file_run,'New':val,'ErrorMessage':None})
    self.__file_run = str(val)

  @file_movie.setter
  def file_movie(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'file_movie',
                             'Success':True,'Previous':self.__file_movie,'New':val,'ErrorMessage':None})
    self.__file_movie = str(val)

  @file_solute.setter
  def file_solute(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'file_solute',
                             'Success':True,'Previous':self.__file_solute,'New':val,'ErrorMessage':None})
    self.__file_solute=str(val)

  @file_traj.setter
  def file_traj(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'file_traj',
                             'Success':True,'Previous':self.__file_traj,'New':val,'ErrorMessage':None})
    self.__file_traj=str(val)

  @outputLocation.setter
  def outputLocation(self,val):
    val = str(val).upper()
    if val in ["FILE","TERMINAL"]:
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'outputLocation',
                               'Success':True,'Previous':self.__outputLocation,'New':val,
                               'ErrorMessage':None})
      self.__outputLocation = val
    else:
      errorMessage = ("Error setting outputLocation. Allowed values are \"file\" and \"terminal\" "
        "(any case).")
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'outputLocation',
                               'Success':False,'Previous':self.__outputLocation,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'IO',
                              'Variable':'outputLocation','ErrorMessage':errorMessage})

  @run_num.setter
  def run_num(self,val):
    if utilities.is_integer(val):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'run_num',
                               'Success':True,'Previous':self.__run_num,'New':val,'ErrorMessage':None})
      self.__run_num=val
    else:
      errorMessage = "Error setting run_num. Must be an integer."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'run_num',
                               'Success':False,'Previous':self.__run_num,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'IO',
                              'Variable':'run_num','ErrorMessage':errorMessage})

  @suffix.setter
  def suffix(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'suffix',
                             'Success':True,'Previous':self.__suffix,'New':val,'ErrorMessage':None})
    self.__suffix=str(val)

  @L_movie_xyz.setter
  def L_movie_xyz(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'L_movie_xyz',
                               'Success':True,'Previous':self.__L_movie_xyz,'New':val,
                               'ErrorMessage':None})
      self.__L_movie_xyz = val
    else:
      errorMessage = "Error setting L_movie_xyz. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'L_movie_xyz',
                               'Success':False,'Previous':self.__L_movie_xyz,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'IO',
                              'Variable':'L_movie_xyz','ErrorMessage':errorMessage})

  @L_movie_pdb.setter
  def L_movie_pdb(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'L_movie_pdb',
                               'Success':True,'Previous':self.__L_movie_pdb,'New':val,
                               'ErrorMessage':None})
      self.__L_movie_pdb = val
    else:
      errorMessage = "Error setting L_movie_pdb. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'L_movie_pdb',
                               'Success':False,'Previous':self.__L_movie_pdb,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'IO',
                              'Variable':'L_movie_pdb','ErrorMessage':errorMessage})

  @file_cbmc_bend.setter
  def file_cbmc_bend(self,val):
    self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'file_cbmc_bend',
                             'Success':True,'Previous':self.__file_cbmc_bend,'New':val,
                             'ErrorMessage':None})
    self.__file_cbmc_bend = str(val)

  @ltraj.setter
  def ltraj(self,val):
    if isinstance(val,bool):
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'ltraj',
                               'Success':True,'Previous':self.__ltraj,'New':val,'ErrorMessage':None})
      self.__ltraj = val
    else:
      errorMessage = "Error setting ltraj. Must be a boolean."
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'IO','Variable':'ltraj',
                               'Success':False,'Previous':self.__ltraj,'New':val,
                               'ErrorMessage':errorMessage})
      self.__errorLog.append({'Date':datetime.datetime.now(),'Type':'Setter','Module':'IO',
                              'Variable':'ltraj','ErrorMessage':errorMessage})
