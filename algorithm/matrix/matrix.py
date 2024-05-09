def shape(matrix):  
  n = len(matrix)
  m = len(matrix[0])
  return (n,m)

def rotate(mat):
  n,m = shape(mat)  
  rotated_mat = [[0]*n for _ in range(m)]
  
  for i in range(n):
    for j in range(m):      
      rotated_mat[j][n-i-1]=mat[i][j]
  
  return rotated_mat      

def transpose(matrix):
  n,m = shape(matrix)
  t_matrix = [[0]*n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      t_matrix[j][i] = matrix[i][j]
  return t_matrix


 
 


def display(matrix):
  n,m = shape(matrix) 
  print(f'({n} rows, {m} columns)')
  for row in matrix:
    print(row)