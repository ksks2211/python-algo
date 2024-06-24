# Question
# (A) N개의 여행지 1 <= N <= 500
# (B) 여행지 간에 도로가 존재하는 경우 양방향 이동가능
# (C) M개의 도시로 이루어진 여행계획이 주어짐(중복가능) 1 <= M <= 500
# 여행 가능여부 출력


# Solution
# 거리는 무관하고 도달가능 여부가 중요함
# 출발점에서 BFS 해서 각 점에 도달여부만 체크
from collections import deque

def get_result(graph, travel_plan):
  
  visited = { key : False for key in graph.keys()}  
  q = deque([travel_plan[0]])
  
  
  while q:
    cur = q.popleft()
    if visited[cur]: continue    
    visited[cur]= True        
    for neighbor in graph[cur]:
      q.append(neighbor)
      
  return all(visited[city] for city in set(travel_plan))




graph = {
  1 : [2,4,5],
  2 : [1,3,4],
  3 : [2],
  4 : [1,2],
  5 : [1]
}

travel_plan = [2,3,4,3]

print(get_result(graph,travel_plan ))


# Solution2
# 서로소 집합을 이용
# 여행계획에 존재하는 모든 노드가 같은 parent를 공유한다면 연결

def find(parent, v):
  if parent[v]!=v:
    parent[v] = find(parent, parent[v])
  return parent[v]   

def union(parent, v,w):
  vp = find(parent, v)
  wp = find(parent,w)
  
  if vp < wp:
    parent[wp] = vp
  else:
    parent[vp] = wp
  

def get_result2(edges, travel_plan, vertices):
    
  parent = { v : v for v in vertices}  
  
  for v, w in edges:    
    union(parent, v,w)
    
  
  return 1 == len(set(parent[city] for city in set(travel_plan)))
  
  
edges = [(1,2),(1,4),(1,5),(2,3),(2,4)]

print(get_result2(edges, travel_plan, [1,2,3,4,5]))





