# Question
# (A) 1 ~ N 까지의 도시 , 1 <= N <=30,000
# (B) M 개의 도시간 통로, 1 <= M <= 200,000
# (C) 통로 마다 지나는데 시간Z 소요  1<= Z <=1,000
# 도시 C를 출발해서 도달 가능한 모든 도시로 메시지 전달
# 걸리는 시간 + 도시의 개수



# Solution
# 다익스트라 알고리즘
# 도달 가능한 도시 : distances 에서 INF가 아닌 점과 출발점을 제외
# 걸리는 시간 : distances 에서 INF가 아닌 점 중 최대값

import heapq
from collections import defaultdict

def get_result(n, edges,start):
  INF = float('infinity')
  distances = { v : INF for v in range(1,n+1)}
  
  graph = defaultdict(list)
  
  for x,y, cost in edges:
    graph[x].append((cost, y))
    
  
  distances[start] = 0
  
  
  q = [(0, start)]
  
  
  while q:    
    cur_dist, cur_vertex = heapq.heappop(q)    
    if distances[cur_vertex] < cur_dist : continue
    
    for cost, neighbor in graph[cur_vertex]:
      
      dist = cost + cur_dist
      
      if dist < distances[neighbor] :
        distances[neighbor] = dist
        heapq.heappush(q, (dist, neighbor))
      
              
  result = list(filter(lambda x:x!=INF and x!=0, distances.values()))
  
  return (len(result), max(result))




print(get_result(3, [(1,2,4),(1,3,2)], 1) )