# Question
# (A) 정수 X가 주어진다 1<=X<=30,000
# (B) 연산1 - 5로 나누기(나누어 떨어지는 경우)
# (C) 연산2 - 3으로 나누기(나누어 떨어지는 경우)
# (D) 연산3 - 2로 나누기(나누어 떨어지는 경우)
# (E) 연산4 - 1빼기
# 연산을 사용해서 숫자를 1로 만들때, 가장 적은 연산횟수로 1을 만드는 연산횟수는

from collections import deque, defaultdict

# Solution
# Memoization + BFS
# memo = visited x set
# 1에서 시작해서 역연산으로 x 까지 도달
# 수가 x보다 커지면 탐색종료(백트래킹)
# 이미 기록된 경우엔 연산하지 않기

# 점화식 f(n) = min(f(n-1), f(n//2), f(n//3), f(n//5)) + 1 
def get_result(x):          
  count = 0       
  q = deque()
  q.append((1, 0))

  memo = set()
 
  while q:    
    # 현재 숫자, 연산 횟수
    cur, count = q.popleft()
    
    # 종료조건
    if cur == x : break    
    
    
    if cur in memo : continue    
    
    memo.add(cur)
    
    if cur+1 <= x : q.append((cur+1, count+1))
    if cur*2 <= x : q.append((cur*2, count+1))
    if cur*3 <= x : q.append((cur*3, count+1))
    if cur*5 <= x : q.append((cur*5, count+1))
   
  return count


# Dynamic Programming
# dp[n] : 숫자 1에서 n이 되는 최소 연산횟수
# 시간복잡도 : O(N)
def get_result2(x):  
  dp = [0]*(x+1)    
  for i in range(2, x+1):    
    dp[i] = dp[i-1]+1
    if i%2==0 : dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0 : dp[i] = min(dp[i], dp[i//3]+1)
    if i%5==0 : dp[i] = min(dp[i], dp[i//5]+1)

  return dp[x]  

# Memoization
# recursive
def get_result3(x, memo = defaultdict(int)):
  if x<=1 : return 0
  
  if x in memo : return memo[x]
  
  memo[x] = get_result3(x-1,memo) + 1
  
  if x%5 == 0 : memo[x] = min(memo[x], get_result3(x//5)+1)
  if x%3 == 0 : memo[x] = min(memo[x], get_result3(x//3)+1)
  if x%2 == 0 : memo[x] = min(memo[x], get_result3(x//2)+1)
  
  
  return memo[x]
  

print(get_result(26))
print(get_result2(26))
print(get_result3(26))