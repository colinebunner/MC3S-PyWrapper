import datetime

class changeLog:

  allKeys = ["Date","Location","Index","Variable","New","Previous","Success","ErrorMessage"]

  def __init__(self):
    super().__init__()
    self._data = []

  def append(self, item, ignoreMissing = False):
    # check that item is dict
    if not isinstance(item,dict):
      print("Scream")

    keys = item.keys()

    # Check that no ridiculous keys are being passed
    for key in keys:
      if not key in changeLog.allKeys:
        print("Oh no!")

    # Add Index = None if the variable is not a oneDimArray, and so doesn't need to track an index
    if not "Index" in keys and ignoreMissing == False:
      item["Index"] = None

    # Add ErrorMessage = None if one isn't passed
    if not "ErrorMessage" in keys and ignoreMissing == False:
      item["ErrorMessage"] = None

    self._data.append(item)

  def copy(self):

    newCHL = changeLog()

    for ch in self._data:
      newCHL.append(ch)

    return newCHL

  def returnAbbreviated(self, keys):
    ''' Returns a new changeLog that only contains entries for the specified keys
        Input:  keys (list() of indices to keep)
        Output: A changeLog with entries only for the specified keys

        Available keys (case-sensitive):
          - Date      (datetime object created when change was made)
          - Location  (string to id where the variable is located [Sim/---])
          - Index     (only present for variables that are oneDimArrays, which index (starting at 1) is being referred to)
          - Variable  (string matching variable changed)
          - New       (value passed to the variable setter)
          - Previous  (previous value stored for that variable)
          - Success   (True: the variable was successfully changed from 'Previous' to 'New', False: you can figure it out)
          - ErrorMessage (If Success == False, what went wrong. Otherwise None.)'''

    newCHL = changeLog()

    for ch in self._data:
      newDict = {}
      for key in keys:
        newDict[key] = ch[key]
      newCHL.append(newDict, ignoreMissing = True)

    return newCHL

  def returnMask(self, maskDict):
    ''' Returns a new changeLog that only contains entries that fulfill specified key/value pairs
        Input:  maskDict (dictionary of key/value pairs)
        Output: A changeLog with only the entries that match the specified key/value pair

        Available keys (case-sensitive):
          - Date      (datetime object created when change was made)
          - Location  (string to id where the variable is located [Sim/---])
          - Index     (only present for variables that are oneDimArrays, which index (starting at 1) is being referred to)
          - Variable  (string matching variable changed)
          - New       (value passed to the variable setter)
          - Previous  (previous value stored for that variable)
          - Success   (True: the variable was successfully changed from 'Previous' to 'New', False: you can figure it out)
          - ErrorMessage (If Success == False, what went wrong. Otherwise None.)'''

    newCHL = changeLog()

    # For single key/value pairs, turn values into list
    newMask = {}
    for key in maskDict.keys():
      if not isinstance(maskDict[key],list):
        newMask[key] = [maskDict[key]]
      else:
        newMask[key] = maskDict[key]

    keys = newMask.keys()

    for ch in self._data:
      logic = True
      for key in keys:
        if not ch[key] in newMask[key]:
          logic = False
      if logic:
        newCHL.append(ch,ignoreMissing=True)

    return newCHL

  @property
  def data(self):
    return self._data
