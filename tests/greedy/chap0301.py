# Question
# (A) N원을 동전으로 거슬러 주는 상황
# (B) N은 10의 배수
# (C) 500, 100, 50, 10 개의 동전이 무한개
# (D) 동전의 개수를 최소화 
# 동전의 개수는?
  
# Solution
# - 거스름돈을 돌려주는 것이 불가능한 경우는 없음
# - 큰 동전은 항상 작은 동전n개와 동일함
#   - 따라서 큰 동전이 사용가능한 경우에는 항상 큰 동전을 사용
#   - e.g. 100원 1개   <  50원 2개 < 50원 1개 + 10원 5개
# - Greedy 알고리즘 : 가장 큰 단위로 최대한 거슬러주기 반복


# Time Complexity : O(K) 
# K : 동전의 종류의 수 = 4

def get_result(N):  
  coins = [500,100,50,10]    
  result = 0
  
  for coin in coins:
    
    # Skip
    if N < coin : continue            
    
    
    # 몫, 나머지
    share, N = divmod(N,coin)    
    result += share
        
    if N == 0 : break
  return result


assert get_result(1260)==6, "Unexpected Result"
    
    
    
    
    

