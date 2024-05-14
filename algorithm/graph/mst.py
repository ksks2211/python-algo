from ..set.disjoint_set import create_parent_table, find, union


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