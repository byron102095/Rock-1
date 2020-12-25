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

# Add two matrix m1 and m2 and return the resulting matrix, return empty array if there's error
def add_matrices(m1,m2):
  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    return []
  if not is_a_valid_matrix(m1) and not is_a_valid_matrix(m2):
    return []
    
  num_rows = len(m1)
  num_cols = len(m1[0])
  m0 = create_matrix(num_rows, num_cols)
  for i in range(num_cols):
    for j in range(num_cols):
      m0[i][j] = m1[i][j] + m2[i][j]
  return m0

##### Sample Questions
matrix = [[4,5,3],
          [7,8],
          [7,-1,-8]]
matrix1 = [[0,1,-32],
          [1,2,1],
          [2,5,0]
#######



def is_a_valid_matrix(matrix):
  if m == []:
   return False
  for i in matrix:
    if i != num_cols:
      False
  return True

