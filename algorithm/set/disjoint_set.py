def create_parent_table(vertices:list):  
  parent = { v : v for v in vertices}  
  return parent

def find(parent:dict, x):  
  if parent[x] != x : 
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent:dict, a, b):
  
  ap = find(parent,a)
  bp = find(parent,b)
  
  if ap < bp:
    parent[bp]  = ap
  else:
    parent[ap]  = bp
    