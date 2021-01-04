def is_increasing(lst):
  if not lst:
    return False
  elif len(lst) < 2:
    return True
  else:
    return lst[0] < lst[1] and is_increasing(lst[1:])

lst1 = [2,2,3]