import datetime

def datetimePrettify(dtObj):

  return "{}/{}/{}\t{}:{}:{}:{}".format(dtObj.month,dtObj.day,dtObj.year,dtObj.hour,dtObj.minute,dtObj.second,dtObj.microsecond)
