#Recursion: Fibonacci

# f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2)

def fib(n):
  if n == 0:
    return 0 
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

def fibs(n):
  x = 0
  # Given
  n0 = 0
  n1 = 1
  # Base case
  if n == 0:
    return 0
  elif n == 1:
    return 1
  #Recursion - Using while loop
  else:
    while x < n:
      nth = n0 + n1
      # Update values
      n0 = n1
      n1 = nth
      x += 1
    return nth