# Question
# A - N x N 크기의 2차원 공간, 2 <= N <= 125
# B - 출발지점(0,0)에서 목표지점(N-1, N-1)까지 최적의 경로 찾기
# C - 상하좌우로 1칸씩 이동
# D - 각 칸에는 해당 칸을 지나기 위한 비용이 존재
# E - 0 <= 비용 <= 9

import heapq

# Solution
# 다익스트라 최단거리 알고리즘
# V = N x N = 정점의 개수
# E = N x (N - 1) x 2 = 간선의 개수


INF = float('infinity')

def get_result(N, cost_matrix):
    
  dirs = [(0,1),(1,0),(0,-1),(-1,0)]
  
  def validate(x,y):
    return 0<=x< N and 0<=y < N 
    
  shortest_paths = [[INF]*N for _ in range(N)]  
  shortest_paths[0][0] = cost_matrix[0][0]
  
  q = [(shortest_paths[0][0],0 ,0)]
  
  while q:    
    cur_dist, cur_x, cur_y = heapq.heappop(q)    
    
    if cur_x == N-1 and cur_y == N-1 : break
    
    if shortest_paths[cur_x][cur_y] < cur_dist: continue
        
    for dx, dy in dirs:
      nx, ny = dx+cur_x, dy+cur_y
      if not validate(nx, ny): continue      
      new_dist = cur_dist + cost_matrix[nx][ny]
      
      if new_dist < shortest_paths[nx][ny]:
        shortest_paths[nx][ny] = new_dist
        heapq.heappush(q, (new_dist, nx, ny))
            
  return shortest_paths[N-1][N-1]





N = 3
matrix = [
  [5,5,4],
  [3,9,1],
  [3,2,7]
]

print(get_result(N, matrix))


N = 5
matrix = [
  [3,7,2,0,1],
  [2,8,0,9,1],
  [1,2,1,8,1],
  [9,8,9,2,0],
  [3,6,5,1,5]
]

print(get_result(N, matrix))


N = 7
matrix = [
  [9,0,5,1,1,5,3],
  [4,1,2,1,6,5,3],
  [0,7,6,1,6,8,5],
  [1,1,7,8,3,2,3],
  [9,4,0,7,6,4,1],
  [5,8,3,2,4,8,3],
  [7,4,8,4,8,3,4]
]

print(get_result(N, matrix))