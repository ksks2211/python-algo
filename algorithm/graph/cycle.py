from ..set.disjoint_set import create_parent_table, find, union


# Un-Directed Graph
def has_cycle(vertices, edges):
  
  parent = create_parent_table(vertices)
  
  for v,w in edges:
    if find(parent,v) == find(parent,w):
      return True
    else : 
      union(parent, v, w)
  return False



# Directed Graph
