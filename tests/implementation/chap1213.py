# Question
# - N X N 크기의 도시, 2 <= N <=50
# - 집의 치킨거리 : 집에서 가장가까운 치킨집까지의 거리
# - 도시의 치킨거리 : 위의 합
# - 치킨집 중에서 M개를 고르고 나머지 제거, 1 <= M <= 13
# - 빈칸, 치킨집, 집
# -  1 <= 집의 개수 < 2N
# -  M <= 치킨집의 개수 <= 13
# - 도시의 치킨거리가 가장 최소가 되도록 M개를 고를때의 치킨거리 출력




# Solution
# X개(최대 13)의 치킨집에서 M개를 순서없이 뽑기 => 조합 
# 치킨거리 => 각 집에대해서 각 치킨집과의 맨해튼 거리를 측정해서 가장 가까운것 선택
# memo : 한 집과 한 치킨집의 거리 (재사용 가능)
from itertools import combinations




INF = float('infinity')

def get_distance(home, chicken):
  x, y = home
  a, b = chicken  
  return abs(x-a) + abs(y-b)

def get_result(M, homes, chickens):
  
  total_dist = INF
  
  
  
  A = len(homes)
  B = len(chickens)
  
  
  
  # distance[a][b]
  distances = tuple( tuple(get_distance(home, chicken) for chicken in chickens) for home in homes)
  
  
  for chickens_idx in combinations(range(B), M):
    new_dist = sum(min(row[i] for i in chickens_idx) for row in distances)
    total_dist = min(total_dist, new_dist)
  
  return total_dist




N = 5
homes = [(0,2), (1,4),(2,1),(3,2)]
chickens = [(1,2),(2,2),(4,4)]
M = 3

print(get_result(M, homes, chickens))



homes = [(0,3),(1,0),(1,2),(3,3),(3,4),(4,3)]
chickens = [(0,1),(3,0),(4,0),(4,1),(4,4)]
M = 2
print(get_result(M, homes, chickens))



homes = [(0,0),(1,0),(2,0),(3,0),(4,0)]
chickens = [(0,1),(1,1),(2,1),(3,1),(4,1)]
M = 1
print(get_result(M, homes, chickens))



homes = [(0,0),(1,0),(2,0),(3,0),(4,0), (0,4),(1,4),(2,4),(3,4),(4,4)]
chickens = [(0,1),(1,1),(2,1),(3,1),(4,1), (0,3),(1,3),(2,3),(3,3),(4,3)]
M = 1
print(get_result(M, homes, chickens))