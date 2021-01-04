def intersection(lst1,lst2):

  # base case
  if len(lst1) == 0:
    return []
  # check if the first term matches
  elif lst1[0] in lst2: #if it does
    one_copy = check_copies(lst1,lst2,lst1[0]) #check list for copies and do it again!
    return one_copy
  else: # if it doesn't
    return intersection(lst1[1:],lst2) # do it again!
  
def check_copies(lst1,lst2,n):

  #if copies of list is more than or equal to 2
  if lst1.count(n) >= 2:
    #skip and continue with recursion
    return intersection(lst1[1:],lst2)
  else:
    #if no copies of n, return n and continue recursion
    return [n] + intersection (lst1[1:],lst2)

lst1 = [1,2,3]
lst2 = [1,2,3]