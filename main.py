def fizzbuzz(n):
  while n >= 0:
    n -=1
    if (n+1) % 3 == 0 and (n+1) % 5 ==0:
      print("fizzbuzz")
    elif (n+1) % 3 == 0:
      print("fizz")
    elif (n+1) % 5 == 0:
      print('fizzbuzz')
    else:
      print(n+1)