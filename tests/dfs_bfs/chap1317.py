# Question
# (A) N x N 크기의 시험관
# (B) 1~k 의 바이러스 
# (C) 바이러스는 상하좌우 방향으로 증식
# (D) 번호가 낮은것 부터 증식
# (E) 다른 바이러스가 존재하는 칸에는 증식 불가능
# 목표 : S 초 뒤에 X,Y 지점에 존재하는 바이러스 출력 => 없으면 0


# Solution
# BFS + Heapq
# element  =  (time, virus_num, a,b) 
# contaminate(matrix, v_type, x,y)  x, y 지점의 상하좌우가 0이면 증식
# 반복문
# 반복조건 q.empty() == False 
# t, v_type, a, b = heapq.heappop(q)  일 때
#   t > S : break

# 시간복잡도 
# bfs O(N^2)
# 정렬 O(N^2 logN)

import heapq
from collections import deque

dirs = [(0,1),(-1,0),(1,0),(0,-1)]

def get_priority_queue(matrix, n):
  q = []
  for i in range(n):
    for j in range(n):
      if matrix[i][j] !=0:
        heapq.heappush(q, (0, matrix[i][j], i, j))
  
  return q      
      
def get_sorted_queue(matrix, n):
  q = []
  for i in range(n):
    for j in range(n):
      if matrix[i][j] !=0:
        q.append((0, matrix[i][j], i, j))
  
  q.sort()
  return deque(q)


def get_result(matrix, S, x, y):
  
  x, y = x-1, y-1
  if S == 0 : return matrix[x][y]

  n = len(matrix)    
  q = get_priority_queue(matrix, n)
      
  while q:            
    t, v_type, a, b = heapq.heappop(q)   
        
    for dx, dy in dirs:
      nx, ny = dx+a, dy+b  
      if 0<=nx < n and 0<=ny < n and matrix[nx][ny] == 0 :
        matrix[nx][ny] = v_type 
        if nx == x and ny ==y :  return matrix[x][y]          
        
        if t +1 < S : heapq.heappush(q, (t+1, v_type, nx, ny))
  
  return matrix[x][y]
  
  


def get_result2(matrix, S, x, y):
  x, y = x-1, y-1
  if S == 0 : return matrix[x][y]      
  
  n = len(matrix)  
  q = get_sorted_queue(matrix, n)
  
  while q :    
    t, v_type, a, b = q.popleft()    
    for dx, dy in dirs:
      nx, ny = dx+a, dy+b  
      if 0<=nx < n and 0<=ny < n and matrix[nx][ny] == 0 :
        matrix[nx][ny] = v_type 
        if nx == x and ny ==y :  return matrix[x][y]
          
        if t +1 < S : q.append((t+1, v_type, nx, ny))

  return matrix[x][y]

matrix = [[1,0,2],[0,0,0],[3,0,0]]

print(get_result2(matrix, 2, 3, 2))


matrix = [[1,0,2],[0,0,0],[3,0,0]]

print(get_result2(matrix, 1,2,2))