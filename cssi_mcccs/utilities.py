import numpy as np

def is_number(val):
  try:
    v = float(val)
    return True
  except ValueError:
    return False

def is_integer(val):
  return (isinstance(val,int) or isinstance(val,np.int8) or isinstance(val,np.int16) or 
          isinstance(val,np.int32) or isinstance(val,np.int64))

def is_positive_integer(val):
  if is_integer(val):
    return val > 0
  else:
    return False
