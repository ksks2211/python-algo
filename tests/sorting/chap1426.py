# Question
# (A) 정렬된 두 묶음의 숫자카드 합치기(A + B)의 비교 필요
# (B) 여러개의 카드 묶음이 존재할때 합치는 최소 비교수 출력



# Solution
# Merge 횟수는 항상 N-1 번
# 가장 먼저 Merge 된 묶음 => N-1 배
# 가장 나중에 Merge된 묶음 => 1 배
# 항상 작은것 부터 Merge 하는것이 유리
import heapq


def get_result(batches):
  
  
  if len(batches)==1 : return 0
  
  batches.sort()
  
  heapq.heapify(batches)
  
  count = 0
  while len(batches) > 1 :
    a = heapq.heappop(batches)
    b = heapq.heappop(batches)    
    count += (a+b)
    heapq.heappush(batches, a+b)  
    
  return count    
  
  
  
print(get_result([10,20,40]))
  
  