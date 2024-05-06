# Question
# (A) N x M 크기의 직사각형
# (B) 1로는 이동가능, 0 으로는 이동 불가능 출발점(1,1) 도착점(N,M)
# (C) 항상 도착가능경로 존재
# 최소경로에 필요한 칸의 개수



# Solution
# BFS를 이용
# 방문상태를 저장할 행렬 

from collections import deque


def check(n,m,i,j):
  if 0<=i<n and 0<=j<m : return True
  return False

def get_result(n,m, graph):
    
  dx=[0,0,1,-1]
  dy=[1,-1,0,0]  
  q = deque([(0,0)])  
  visited = [[False]*m for _ in range(n)]
  
  while q:
    i,j = q.popleft()
    
    if visited[i][j] or graph[i][j]==0: continue
    
    visited[i][j]=True
   
    # 종료조건
    if i==n-1 and j==m-1:break
    
    
    for k in range(4):      
      ni, nj = i+dx[k], j+dy[k]
      
      # valid & not visited
      if check(n,m,ni,nj) and not visited[ni][nj]:         
        graph[ni][nj] = graph[i][j]+1
        q.append((ni,nj))


  for r in graph:
    print(r)
          
  return graph[n-1][m-1]



graph = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]


print(get_result(5,6,graph))


graph = [[1,1,0],[0,1,0],[0,1,1]]


print(get_result(3,3,graph))
