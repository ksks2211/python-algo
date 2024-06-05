# Question
# (A) N x M 크기의 직사각형
#   3 <= N, M <= 8    
# (B) 0=빈칸, 1=벽, 2=바이러스
#   항상 빈칸의 수는 3개 이상
# (C) 새로 만들수 있는 벽의 개수는 3개, (빈칸 => 벽)
# (D) 바이러스는 상하좌우로 퍼져나감, 벽으로 막히면 못나감
# 안전영역의 최대크기



# Solution
# empties = [(x,y), ...]
# viruses = [(x,y),...]
# 빈칸을 벽으로 바꾸는 경우의수
# 64개에서 3개를 순서없이 뽑기 (조합) =>  64 x 21 x 31 가지 ~= 4만
# 3점을 벽으로 바꾸기 0 => 1
# 각 경우에 바이러스에서 출발하는 dfs or bfs 하고 0 => 2 카운트


# 시간복잡도 O(nm)

from itertools import combinations
from collections import deque

def validate(i,j, n,m):  
  if 0<=i<n and 0<=j<m : return True  
  return False




def bfs(matrix, i,j, n, m ):  
  q = deque()  
  q.append((i,j))  
  dirs = [(0,1),(1,0),(0,-1),(-1,0)]  
  virus_area = 0    
  while q:    
    x, y  = q.popleft()    
    for dx,dy in dirs:
      nx,ny = x+dx, y+dy
      if validate(nx,ny, n,m) and matrix[nx][ny] == 0 :
        matrix[nx][ny] = 2
        virus_area+=1
        q.append((nx,ny))
    
  return virus_area
  
  
  



def get_result(matrix, empties,  viruses):
  
  n = len(matrix)
  m = len(matrix[0])
  
  result = 0
  for combination in combinations(empties,3):
    area = len(empties) - 3
    
    # Create Wall
    for i, j in combination:      
      matrix[i][j] = 1
    
    # Explore     
    for i,j in viruses:
      area -= bfs(matrix, i,j,n,m)
                
    # Reset matrix + Remove Wall
    for i,j in empties:
      matrix[i][j] = 0

    result = max(result, area)
  
  
  return result





matrix = [
  [2, 0, 0, 0, 1, 1, 0],
  [0, 0, 1, 0, 1, 2, 0],
  [0, 1, 1, 0, 1, 0, 0],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 1],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0]]

empties = [(0, 1), (0, 2), (0, 3), (0, 6), (1, 0), (1, 1), (1, 3), (1, 6), (2, 0), (2, 3), (2, 5), (2, 6), (3, 0), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 0), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 0), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
viruses = [(0, 0), (1, 5)]


print(get_result(matrix, empties, viruses))