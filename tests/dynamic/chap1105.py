from collections import Counter
# Question
# (A) N개의 볼링공 
# (B) A와 B가 서로 무게가 다른 볼링공을 골라야 함
# (C) 볼링공의 무게는 1~M의 자연수
# (D) 동일한 무게의 다른 볼링공 가능
# 공의 무게가 주어질 때, 고를 수 있는 공의 조합의 경우의 수




# Solution
# N개의 공에서 2개를 순서 없이 뽑기
# 조합 = 순서 X
# 불가능한 조합 = 크기가 같은 다른공을 뽑는 조합
# 전체 경우의 수 - 크기가 같은 공을 뽑는 경우의 수



def get_result(weights):
  
  n = len(weights)
  
  
  cnt = Counter(weights)
      
  total = n * (n - 1) // 2
  
  for item in cnt:
    if cnt[item] > 1 : 
      total -= cnt[item] * (cnt[item] - 1 ) // 2
  
  return total



assert get_result([1,3,2,3,2]) == 8
assert get_result([1,5,4,3,2,4,5,2]) == 25