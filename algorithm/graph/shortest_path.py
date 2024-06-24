import heapq


INF = float('infinity')


def dijkstra(graph, start, end):
  
  distances = {
    v : INF for v in graph.keys()
  }  
  distances[start]=0
      
  q=[(0,start)]
      
  while q:
    cur_dist, cur_vertex = heapq.heappop(q)    
    if distances[cur_vertex] < cur_dist : continue
    
    
    
    for neighbor,weight  in graph[cur_vertex]:
      new_dist = cur_dist + weight
                  
      if new_dist < distances[neighbor]:        
        distances[neighbor] = new_dist
        heapq.heappush(q, (new_dist, neighbor))
  
  return distances[end]    

def dijkstra_path(graph, start,end):

  distances = {
    v : INF 
    for v in graph.keys()
  }
    
  predecessors = {
    v : None
    for v in graph.keys()
  }
  
  # 초기값
  distances[start]=0
  q = [(0,start)]
  
  
  while q:
    cur_dist, cur_vertex = heapq.heappop(q)    
    if distances[cur_vertex] < cur_dist : continue
            
    for neighbor,weight  in graph[cur_vertex]:
      dist = cur_dist + weight
                  
      if dist < distances[neighbor]:      
        distances[neighbor] = dist
        predecessors[neighbor] = cur_vertex
        heapq.heappush(q, (dist, neighbor))
  
  
  # Route from start to end
  path = [end]  
  cur = end  
  while cur!=start:
    path.append(predecessors[cur])
    cur = predecessors[cur]
  
  return path[::-1]         
              
def floyd_warshall(edges, n):
  distances = [[INF]*(n+1) for _ in range(n+1)]
  
  for i in range(1,n+1):
    distances[i][i] = 0
  
  for x,y,weight in edges:
    distances[x][y] = weight
      
  for k in range(1,n+1):
    for i in range(1,n+1):            
      for j in range(1,n+1):
        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        
  return distances
  
 