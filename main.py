# Matrices
# Create a 0 matrix of size m x n where m is the number of rows and n is the number of compile
def create_matrix(m,n):
  my_matrix = []
  for i in range(m):
    my_row = []
    for j in range(n):
      my_row.append(0)
    my_matrix.append(my_row)
  return my_matrix

def is_a_valid_matrix(matrix):
  num_cols = len(matrix[0])
  #empty
  if matrix == []:
    return False
  # Columnns dont match up on each row
  for i in matrix:
    if len(i) != num_cols:
      return False
  return True

def multiply_matrix(m1,m2):
  if not is_a_valid_matrix(m1) or not is_a_valid_matrix(m2):
    print("not valid")
    return []
  num_rows = len(m1)
  num_cols = len(m2[0])
  if not len(m1[0]) == len(m2):
    print("not same nxm")
    return []
  m0 = create_matrix(num_rows,num_cols)
  i = 0
  j = 0
  while i < num_rows:
    while j < num_cols:
      for x in range(len(m1[0])):
        m0[i][j] += m1[i][x]*m2[x][j]
        print(m0)
      j += 1
    j = 0
    i += 1
  return m0