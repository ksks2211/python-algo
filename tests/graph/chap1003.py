# Question
# (A) N개의 집과 M개의 길, 임의의 두 집 사이에 경로가 항상 존재
# (B) 길에는 유지비C가 존재  1<= C <= 1,000
# (C) 집을 a마을 b마을로 분리
# (D) 마을에는 집이 1개 이상 존재
# (E) 마을 안의 두 집 사이에는 항상 길이 존재 (Connected Graph)



# Answer
# 최소비용 신장트리 이용
# Cost를 순서대로 기록할 배열 만들기
# 크루스칼 알고리즘으로 최소비용 신장트리 찾기
# 가장 마지막 Edge 제거하기



def union(parent, a,b):  
  a,b = find(parent, a), find(parent, b)  
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def find(parent, x):
  if parent[x]!=x:
    parent[x] = find(parent, parent[x])
  return parent[x]  


def get_result(vertices, edges):
    
  parent = { v:v for v in vertices}            
  edges.sort(key=lambda x : x[2])
  costs =[]
  
  for a,b, cost in edges:
    
    pa, pb = find(parent, a), find(parent,b)
    
    # Cycled
    if pa == pb : continue
    
    # Un-Cycled
    union(parent, pa,pb)
    costs.append(cost)
    
  return sum(costs[:-1])
  
  
  
  
  


edges = [
  (1,2,3),
  (1,3,2),
  (3,2,1),
  (2,5,2),
  (3,4,4),
  (7,3,6),
  (5,1,5),
  (1,6,2),
  (6,4,1),
  (6,5,3),
  (4,5,3),
  (6,7,4)
]


print(get_result(vertices=[1,2,3,4,5,6,7], edges= edges))