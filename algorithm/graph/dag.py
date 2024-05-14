from collections import deque

def graph_to_edges(graph, vertices):  
  edges = []  
  for v in vertices:
    for neighbor in graph[v]:
      edges.append((v,neighbor))
  return edges


def topological_sort(graph, vertices):
  
  edges = graph_to_edges(graph, vertices)
  
  result = []    
  in_degrees = { v : 0 for v in vertices}
  
   
  for v,w in edges:
    in_degrees[w]+=1
  
  S = deque( v for v in in_degrees.keys() if in_degrees[v]==0)
  
  while S:
    v  = S.popleft()
    result.append(v)
    for w in graph[v]:
      in_degrees[w]-=1
      if in_degrees[w]==0: S.append(w)
  
  return result if len(result) == len(vertices) else None
  
  