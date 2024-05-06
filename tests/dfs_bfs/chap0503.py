# Question
# (A) N x M 크기의 얼음틀, 1 <= N,M <=1,000
# (B) 0 or 1 , 0이 상하좌우 붙은건 연결된것으로 간주
# 얼음 조각의 개수


# Solution
# map[i][j] 를 출발하는 dfs or bfs,  방문한 노드는 1로 표시
# 상하좌우 => 우하만 탐색해도 결과동일 
#   cur = map[i][j] 인 경우 => map[i+1][j], map[i][j+1]을 탐색대상으로
# 범위를 벗어나는 경우 탐색하지 않기 => i,j 가 범위를 벗어나는지 체크하는 함수


def check(n,m,i,j):
  if 0<=i<n and 0<=j<m : return True
  return False
  

def dfs(n, m, graph, i,j):  
  # visit
  graph[i][j]=1
  if check(n,m,i+1,j) and graph[i+1][j]==0: dfs(n,m,graph,i+1,j)  
  if check(n,m,i,j+1) and graph[i][j+1]==0: dfs(n,m,graph,i,j+1)
      
  


def get_result(n, m, graph):
  
  count = 0
    
  for i in range(n):
    for j in range(m):      
      if graph[i][j]==0 : 
        count+=1
        dfs(n,m,graph,i,j)
  
  
  return count
  
  


graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]  




print(get_result(4,5,graph))

graph = [[0,0,1],[0,1,0],[1,0,1]]


print(get_result(3,3,graph))
