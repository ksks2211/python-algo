from collections import deque


def dfs_recursive(graph,vertex, visited=set()):
    
  # Visit vertex
  visited.add(vertex)
  print(vertex, end=' ')
  
  for neighbor in graph[vertex]:
    if neighbor not in visited:
      dfs_recursive(graph, neighbor, visited)
  
  
def dfs_iterative(graph,start, visited=set()):
  
  stack = [start]
  
  while stack:
    vertex = stack.pop()
        
    if vertex not in visited:
      
      # Visit vertex      
      visited.add(vertex)
      print(vertex, end=' ')
      
      
      # reversed is not necessary
      for neighbor in reversed(graph[vertex]):
        if neighbor not in visited:
          stack.append(neighbor)


def bfs(graph, start, visited=set()):
  
  queue = deque([start])
  
  
  while queue:    
    vertex = queue.popleft()
        
    if vertex not in visited:
      
      # Visit vertex    
      visited.add(vertex)
      print(vertex, end=' ')
      
      for neighbor in graph[vertex]:
        if neighbor not in visited:
          queue.append(neighbor)
  
  
  

  

  
  