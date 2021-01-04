def filter_gt_n(lst, n):
  if not lst:
    return False
  elif lst[0] == n:
    return True
  else:
    return filter_gt_n(lst[1:],n)