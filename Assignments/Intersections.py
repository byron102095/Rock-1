#Intersection of lists
def intersection(list1, list2):
  solution = [] #Empty set to start us off
  for x in list1:
    for y in list2: #For each value in list1 we will cycle through list2
      if x == y:
        if x not in solution:
          solution.append(x)
        continue
  return solution