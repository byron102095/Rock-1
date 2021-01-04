
# Recursion - Reverse string

def reverse(str):
  # Base Case
  if len(str) < 2:
    return str
  # Recursive Case
  else:
    return reverse(str[1:]) + str[0]

# Printing a list
def print_list(lst):
  if not lst:
    return "Empty"
  else:
    print(lst[0])
    print_list(lst[1:])

def is_in_list(n, lst):
  if not lst:
    return False
  # Recursive case
  else:
    return lst[0] == n or is_in_list(n, lst[1:])