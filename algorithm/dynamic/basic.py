from collections import defaultdict


# Top down
def fibonacci(n, memo = defaultdict(int)):
  # 0 or 1  
  if n<=1 : return n    
  
  
  if n in memo : return memo[n]
  

  result = fibonacci(n-1,memo) + fibonacci(n-2,memo)
  memo[n] = result
  
  return result
  


def fibonacci2(n):
  
  if n<=1 : return n
  
  dp = [0]*(n+1) 
  dp[1] = 1
  
  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
  
  return dp[n]    
  
  