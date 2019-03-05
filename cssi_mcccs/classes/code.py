import datetime
import subprocess
import shlex

class Code:

  def __init__(self,execPath,changeLog=[],errorLog=[]):

    self.__execPath         = execPath
    self.__gitBranch        = None
    self.__gitHash          = None
    self.__buildHost        = None
    self.__preprocDefs      = None
    self.__compilerLocation = None
    self.__changeLog        = changeLog
    self.__errorLog         = errorLog

    getCodeInfo = "{} -v".format(execPath)
    args = shlex.split(getCodeInfo)

    # Set information about code and build if the executable is found
    try:
      version = subprocess.Popen(args,stdout=subprocess.PIPE)
      for i,line in enumerate(version.stdout):
        cl = line.decode("utf-8").strip().split()
        if i==1:
          self.__gitBranch = cl[-1][0:-1]
        elif i==2:
          self.__gitHash = cl[-1]
        elif i==3:
          self.__buildHost = cl[-1]
        elif i==4:
          self.__preprocDefs = cl[-1].split(";")
        elif i==5:
          self.__compilerLocation = cl[-1]

    # Don't let the user proceed without a working executable. Executable not found is likely error.
    except (subprocess.CalledProcessError, OSError) as e:
      errorMessage = ("Type: init\nVar.: Code/__init__\nError: Couldn't set information about code "
        "source and build. Likely couldn't find executable. Proposed path: {}.".format(execPath))
      self.__errorLog.append(errorMessage)


  @property
  def execPath(self):
    return self.__execPath

  @property
  def gitBranch(self):
    return self.__gitBranch

  @property
  def gitHash(self):
    return self.__gitHash

  @property
  def buildHost(self):
    return self.__buildHost

  @property
  def preprocDefs(self):
    return self.__preprocDefs

  @property
  def compilerLocation(self):
    return self.__compilerLocation

  @property
  def errorLog(self):
    return self.__errorLog

  @property
  def changeLog(self):
    return self.__changeLog

  @execPath.setter
  def execPath(self,val):
    # Test code by trying to output version before accepting executable path change
    testCode = "{} -v".format(val)
    args = shlex.split(testCode)
    try:
      version = subprocess.check_output(args)      
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'Code','Variable':'execPath',
                               'Success':True,'Previous':self.__execPath,'New':val,'ErrorMessage':None})
      self.__execPath = val
    except (subprocess.CalledProcessError,OSError) as e:
      errorMessage = ("Type: Setter\nVar.: Code/execPath\nError: Couldn't set new code executable "
        "path. Likely couldn't find executable.")
      self.__errorLog.append(errorMessage)
      self.__changeLog.append({'Date':datetime.datetime.now(),'Module':'Code','Variable':'execPath',
                               'Success':False,'Previous':self.__execPath,'New':val,
                               'ErrorMessage':errorMessage})
