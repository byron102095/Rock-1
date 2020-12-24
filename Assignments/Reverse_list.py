def reverse_list(mylist):
  b = []
  i = 0
  n = 0
  while i < len(mylist):
    b.append(mylist[len(mylist)-1+n])
    n -=1
    i +=1
  return b