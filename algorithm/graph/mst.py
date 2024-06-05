from ..set.disjoint_set import create_parent_table, find, union
import heapq

# edges = (x,y,weight)
def kruskal(edges, vertices):
    
  edges.sort(key=lambda x : x[2])  
  parent = create_parent_table(vertices)
  
  
  min_cost = 0
  
  for a,b, weight in edges:
    a, b = find(parent, a), find(parent,b)
    
    
    # cycled
    if a == b : continue
    
    union(parent, a, b)
    min_cost += weight
  
  
  return min_cost



def prim(graph, vertices, start=1):
  
  
  N = len(vertices)
  
  T = set([start])
  
    
  A = [ (edge[1],edge[0]) for edge in graph[start]]
  
  heapq.heapify(A)
  
  min_cost = 0
  
  while len(T)!=N and A:
    
    weight, v = heapq.heappop(A)
    
    if v in T : continue
    
    
    T.add(v)
    
    min_cost +=weight
    
    for edge in graph[v]:
      heapq.heappush(A, (edge[1],edge[0]))
    
    
  return min_cost
    