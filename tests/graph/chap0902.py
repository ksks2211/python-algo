# Question
# (A) 1 ~ N 까지의 회사, 현재위치 1번  
# (B) 도로 M개, 도로는 항상 양방향, 항상 1시간 소요, 1 <= N, M <= 100
# (C) 이동 경로 1 => K => X
# 최소 시간, 도달 불가능한 경우 -1




# Solution
# 플로이드 워셜 알고리즘 (노드수가 제한적)
def get_result(n, edges, middle, end):
  
  INF = float('infinity')
  distances = [[INF]*(n+1) for _ in range(n+1)]
  
  for i in range(1,n+1):
    distances[i][i] = 0
  
  for x,y in edges:
    distances[x][y] = 1
    distances[y][x] = 1
  
  for k in range(1,n+1):    
    for i in range(1,n+1):
      for j in range(1,n+1):
        distances[i][j] = min(distances[i][j], distances[i][k]+distances[k][j])
        
  
  d1 = distances[1][middle]
  d2 = distances[middle][end]
  
  if d1 == INF or d2 == INF : return -1
  
  return d1 + d2
  



edges = [(1,2),(1,3),(1,4),(2,4),(3,4),(3,5),(4,5)]  

  
print(get_result(5, edges,5, 4) )
  
  

edges = [(1,3),(2,4)]  

print(get_result(4, edges, 4,3))
  
  
  
  
  
  
