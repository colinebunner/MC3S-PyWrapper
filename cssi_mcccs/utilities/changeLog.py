import datetime

class changeLog(list):

  def __init__(self):
    super().__init__()

  def append(self, item):
    super(changeLog, self).append(item)

  def stripLog(self, key, vals):
    # Make a copy of the list
    chLog = self.copy()

    # Loop over all changes in the log and append them to the new changeLog if 
    # the value matches the vals list
    for ch in chLog:
      if ch[key] in vals:
        chLog.append(ch)

    return chLog
