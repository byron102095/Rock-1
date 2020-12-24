def generate_list(start, end, step):
  i = 0
  n = []
  while i < (end + 1 - start)/step:
    n.append(start + i*step)
    i += 1
  return n