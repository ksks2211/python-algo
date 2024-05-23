import heapq
import copy
from collections import deque
# Question
# (A) N개의 강의듣기
# (B) 동시에 여러 강의듣기 가능
# (C) 강의는 선수강의 조건 존재가능
# 각 강의수강 완료에 걸리는 최소시간 찾기 (N개)



# Solution
# 각 과목에 대해서 In-Degree 만들기
# 현재시간 T = 0, 각 과목에 걸리는 시간은 t1, t2, ....
# 완료한 과목 집합 finished=set()
# 반복시작 : finished 가 N이 될 때까지
# In-Degree가 0인 과목만 heapq에 넣기  (T+tn, n)
# heapq에서 하나씩 뽑기   (current_T, n)
#   finished에 있으면 넘어가기
#   finished에 없으면 T = current_T, finished.add(n)
#     In-Degree 업데이트 
def get_result(prerequisites, durations):
  
  N = len(durations.keys())
  
  in_degrees = {
    v : 0 for v in durations.keys()
  }
  
  graph = {
    v : [] for v in durations.keys()
  }
  
  finished = set()
  min_time = dict()
  
  # Convert to Graph + make In_degrees array
  for x,y in prerequisites:
    in_degrees[y]+=1
    graph[x].append(y)
  

  # q
  q = []  
  for v in durations.keys():
    if in_degrees[v]==0: heapq.heappush(q, (durations[v],v))
  
  
  current = 0

  while q and len(finished)!=N:
    current_tmp, v = heapq.heappop(q)
    
    if v in finished : continue

    current = current_tmp
    min_time[v] = current
    finished.add(v)
    
    for neighbor in graph[v]:
      in_degrees[neighbor]-=1
      if in_degrees[neighbor]==0:
        heapq.heappush(q,(current+durations[neighbor],neighbor))
        
  for v in durations.keys():
    print(min_time[v])





# Topological sort를 이용
# 초기값 : min_time 에 durations을 복사
# in_degree의 갱신이 일어날 때 마다 
# min_time[to] = max(min_time[from]+durations[to], min_time[to])
# in_degree[to] 가 0 이 될때의 min_time[to]가 최종결정
def get_result2(prerequisites, durations):
  N = len(durations.keys())
  
  in_degrees = {
    v : 0 for v in durations.keys()
  }
  
  graph = {
    v : [] for v in durations.keys()
  }
  
  min_time = copy.deepcopy(durations)
        
  # Convert to Graph + make In_degrees array
  for x,y in prerequisites:
    in_degrees[y]+=1
    graph[x].append(y)

  q = deque(v for v in in_degrees.keys() if in_degrees[v]==0)
  
  
  while q:
    v = q.popleft()
    
    for w in graph[v]:
      in_degrees[w]-=1
      min_time[w] = max(min_time[w], durations[w]+min_time[v])      
      if in_degrees[w]==0:
        q.append(w)

  for v in durations.keys():
    print(min_time[v])

# 각 강의에 걸리는 시간
durations = {
  1 : 10,
  2 : 10,
  3 : 4,
  4 : 4,
  5 : 3
}

# 각 강의의 선수 관계
prerequisites = [(1,2), (1,3), (3,4),(1,4), (3,5)]


get_result(prerequisites, durations)
print("-----")
get_result2(prerequisites, durations)