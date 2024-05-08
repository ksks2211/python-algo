# Question
# (A) 가로길이 N, 세로길이 2   1 <= N <= 1,000
# (B) 덮개 종류 3가지 2x2, 2x1, 1x2
# 바닥을 채우는 경우의 수


# Solution
# 초기 조건
# f(1) = 1, f(2) = 3
# f(3) = 5, f(4) = 11
# f(n) = f(n-1) + f(n-2) * 2



def get_result(n):
    
    
  dp = [0] * (n+1)
  
  dp[0] = 1
  dp[1] = 1
  
  for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]*2)% 796796
  
  return dp[n]


print(get_result(3))