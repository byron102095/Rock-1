#Will give you the first "n" number of primes
def prime_number(n):
  prime_counter = 0
  start = 2
  while prime_counter < n:
    divider = start
    count = 0
    while divider > 0:
      if (start%divider == 0):
        count += 1
      divider -= 1
    if count == 2:
      prime_counter += 1
      print(start)
    start += 1