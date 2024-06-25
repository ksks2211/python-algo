def shape(matrix):  
  n = len(matrix)
  m = len(matrix[0])
  return (n,m)

def rotate(mat):
  
  # N x M 
  n,m = shape(mat)  
  
  # M x N 
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
    
    
def select_rows(matrix, rows_idx):  
  sub_matrix = [matrix[i][:] for i in rows_idx]
  return sub_matrix    


def select_cols(matrix, cols_idx):
  sub_matrix = [ [ row[i] for i in cols_idx] for row in matrix]
  
  return sub_matrix