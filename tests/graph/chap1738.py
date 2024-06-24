# Question
# - N 명의 성적을 분실, 성적은 모두 다름
# - 학생의 수  2 <= N <= 500
# - 비교한 결과만 가지고 있음
# - 성적 순위가 정확하게 결정되는 학생의 수



# Solution
# 비교 A < B 를  edge A->B 로 바꾸면 방향그래프
# from[v] : V 에서 방문 가능한 점 = V 보다 확실하게 높은점
# to[v] : V 에 도달 가능한 점 = V 보다 확실하게 낮은점
# 순위가 결정되는 경우 :  len(from[v]) + len(to[v]) 가  V - 1 인 경우 => from[v]+1 
# 플로이드 워셜 변형 알고리즘
# 거리 갱신 대신 도달 가능여부만 True or False로 기록


# 순위가 결정되지 않는 경우 : connections[i][j] 에 대해서 not connections[i][j]  and not connection[j][i]



def get_result(edges, n):
  
  connections = [[False]*(n+1) for _ in range(n+1)]
  
  for i in range(1,n+1):
    connections[i][i]=True
    
  for x,y in edges:
    connections[x][y]=True  
    
  for k in range(1,n+1):
    for i in range(1,n+1):
      if not connections[i][k] : continue 
      for j in range(1,n+1):
        if not connections[i][j] and connections[k][j]:
          connections[i][j] = True
       
  
  result=0
  
  
  # 방법-1
  for v in range(1,n+1):
    count_from_vertex = sum(connections[v]) - 1
    count_to_vertex=sum(row[v] for row in connections) - 1
    
    if count_from_vertex + count_to_vertex == n - 1: result+=1
  
  
  # 방법2
  # for i in range(1,n+1):
  #   determined = True  
  #   for j in range(1,n+1):
  #     if not connections[i][j] and not connections[j][i]:
  #       determined=False
  #       break
  #   if determined: result+=1
  
  return result      
    



edges = [
  (1,5),
  (3,4),
  (4,2),
  (4,6),
  (5,2),
  (5,4)
]


print(get_result(edges, 6))



