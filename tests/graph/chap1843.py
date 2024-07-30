# Question
# A - N개의 집과 M개의 집 사이를 연결하는, 1 <= N <= 200,000, N-1 <= M <= 200,000
# B - 도로의 가로등에 대한 비용 = 거리
# C - 임의의 두 집 사이에 가로등이 켜진 경로 존재
# D - 가로등을 최소한으로 사용
# E - 절약가능한 최대 금약


# Solution
# 크루스칼 알고리즘으로 최소비용 신장트리를 찾기
# 최소비용 신장트리의 비용








def get_result(N : int, edges : list):
  
  
  
  # disjoint set
  parent = { i : i for i in range(N)}  
  def find(x):
    if parent[x] != x :
      parent[x] = find(parent[x])  
    return parent[x]    

  def union(x, y):
    px = find(x)
    py = find(y)
    
    if px < py :
      parent[py] = px
    else:
      parent[px] = py
  
  cost_before = sum(map(lambda x : x[2], edges))  
  cost_after = 0
    
  edges.sort(key=lambda x: x[2])
  for v, w, cost in edges:    
    if find(v) == find(w) : continue    

    cost_after+=cost
    union(v,w)
   
  return cost_before - cost_after    



N = 7
edges = [
  (0,1,7),
  (0,3,5),
  (1,2,8),
  (1,3,9),
  (1,4,7),
  (2,4,5),
  (3,4,15),
  (3,5,6),
  (4,5,8),
  (4,6,9),
  (5,6,11)
  ]
  
  
print(get_result(N, edges))