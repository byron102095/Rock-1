def multiply(a, b):
  result = 0
  number_of_additions = 0
  while number_of_additions < abs(b):
    if b >= 0:
      result += a
      number_of_additions += 1
    else:
      result += -a
      number_of_additions +=1

  return result