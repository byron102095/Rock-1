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
  for i in range(num_rows):
    for j in range(num_cols):
      x = 0
      while x < num_cols:
        m0[i][j] += m1[i][0+x]*m2[0+x][j]
        x += 1
        print(m0)
  return m0

m1 = [[3],[1],[3]]
m2 = [[1,2,3]]
    