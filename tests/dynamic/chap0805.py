# Question
# (A) N가지 종류의 화폐 1 <= N <= 100
# (B) 화폐를 사용해서 M을 만들기  1 <= M <= 10,000
# (C) 화폐를 이용한 순서는 영향 없음
#  화폐 개수의 최소



# Solution
# dp[i] : i 가치를 위한 최소 화폐개수
# units = [a, b, c] 일 때
# 초기값 : dp[a] = 1, dp[b] = 1, dp[c] = 1
# 가능 불가능 판단 : 최대공약수의  배수인지 체크
# 점화식 f(n) = min(f(n-a)+1, f(n-b)+1, f(n-c)+1)
import math

def get_result(units, M):
  
  
  # N = len(units)
    
  step = math.gcd(*units)
  if M%step != 0 : return -1
  
  INF = 10001
  dp = [INF]*(M+1)
  
  
  
  # if unit > M => never can be used
  units = [unit for unit in units if unit <= M]
  
  
  dp[0] = 0
  for unit in units:
    dp[unit] = 1
  
  for i in range(step,M+1, step):
    for unit in units:
      if i - unit > 0 and dp[i-unit]!=INF: 
        dp[i] = min(dp[i-unit] + 1, dp[i]) 
  
  return dp[M] if dp[M]!=INF else -1




def recursive(units, memo, m):
  
  INF = 10001
  if m < 0 : return INF
  if m in memo : return memo[m]
  
  tmp = INF
  
  for unit in units:
    if m >= unit :
      tmp = min(tmp, recursive(units, memo, m-unit)+1)
  
  memo[m] = tmp
  return tmp

# recursive
def get_result2(units, M):
  INF = 10001
  
  step = math.gcd(*units)
  if M%step != 0 : return -1
    
  # if unit > M => never can be used
  units = [unit for unit in units if unit <= M]
  
  
  memo = { unit : 1 for unit in units }
  memo[0]=0
  
  
  result = recursive(units, memo, M)
  
  return result if result < INF else -1
  
  

print(get_result([2,3],15))
print(get_result2([2,3],15))

print(get_result([3,5,7],4))
print(get_result2([3,5,7],4))

  
  