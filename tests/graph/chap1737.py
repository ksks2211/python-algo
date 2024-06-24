# Question
# (A) N개의 도시 , 1 <= N <= 100
# (B) M개의 버스, 1<= M <= 100,000
# (C) 버스는  (출발도시, 도착도시, 비용)
# (D) 출발도시 != 도착도시
# (E) 출발도시와 도착도시가 같은 버스 존재가능
# min_costs[i][j] 출력, 갈수 없으면 0


# Solution
# Floyd Warshall 
# index 조정,  도시 N => N-1
def get_result(edges, n):
  
  INF = float('infinity')
  matrix = [[INF]*n for _ in range(n)]
  
  for i in range(n):
    matrix[i][i] = 0
    
    
  for a,b,c in edges:
    matrix[a-1][b-1] = min(c, matrix[a-1][b-1])
  

  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
  
  
  
  
  return [ [ el if el is not INF else 0 for el in r] for r in matrix]
  


edges = [
  [1, 2, 2],
[1 ,3, 3],
[1, 4, 1],
[1, 5, 10],
[2, 4, 2],
[3, 4, 1],
[3, 5, 1],
[4, 5, 3],
[3, 5, 10],
[3, 1, 8],
[1, 4, 2],
[5, 1, 7],
[3, 4, 2],
[5, 2, 4]
]


for row in get_result(edges, 5):
  print(row)
