from collections import defaultdict
import math

# Factorial
def factorial(n):
  if n==0 : return 1  
  
  # return math.factorial(n)
  return n * factorial(n-1)


def factorial_iter(n):    
  result = 1  
  for i in range(1, n+1):
    result *=i
  return result


# Fibonacci
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


def fibonacci_range(n):
  cur, prev = 1, 0
  while cur < n:    
    yield cur
    cur, prev = cur+prev, cur
  


def is_prime(n:int):
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0 : return False
  return True    
  

def get_prime_numbers(n:int)  :
    
  if n < 2 : return []
  
        
  arr = [True]*(n+1)  
  limit = int(math.sqrt(n))+1
  
  
  for i in range(2,limit):
    # Prime number
    if arr[i]:
      m=2
      while i*m <= n :
        arr[i*m]= False
        m+=1
  
  
  return list(i for i in range(2,n+1) if arr[i])
