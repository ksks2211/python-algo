import heapq

# Question
# (A) N개의 도시(=vertices)
# (B) M개의 단방향 도로(=edges), 거리는 1
# (C) X도시에서 출발해 도달가능한 도시중 최단거리가 K인 도시 찾기


# Solution
# (A) 다익스트라 최단경로 알고리즘 
# (B) edges => graph (adj-list)변환

def edges_to_graph(edges, vertices):
  
  graph = {
    v : []
    for v in vertices
  }
  
  
  for x,y in edges:
    graph[x].append(y)
  
  return graph
  

def get_result(edges, vertices, start, k):
  INF = float('infinity')
  
  
  graph = edges_to_graph(edges, vertices)
  dists = {
    v : INF
    for v in vertices
  }
  
  dists[start] = 0
    
  q=[(0, start)]
  
  
  
  while q:    
    dist_to_v, v = heapq.heappop(q)
    if dists[v] < dist_to_v : continue
        
    for neighbor in graph[v]:
      dist_to_n = dist_to_v + 1      
      if dist_to_n < dists[neighbor]:
        dists[neighbor] = dist_to_n
        heapq.heappush(q, (dist_to_n, neighbor))
        
        
  
  results = sorted(v for v in dists.keys() if dists[v] == k )
  
  
  
  
  return results if len(results) > 0  else [-1]
  
        
  



print(get_result(edges=[(1,2),(1,3),(2,3),(2,4)], vertices=[1,2,3,4], start=1, k=2 )  )


print(get_result(edges=[(1,2),(1,3),(1,4)], vertices=[1,2,3,4], start=2, k=1 )  )


print(get_result(edges=[(1,2),(1,3),(2,3),(2,4)], vertices=[1,2,3,4], start=1, k=1 )  )