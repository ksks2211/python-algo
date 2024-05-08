# Question
# (A) 길이가 N 인 배열이 주어진다, 3 <= N <= 100
# (B) 배열의 값은 시걍의 개수 K,  0 <= K <= 1,000
# (C) 배열에서 요소를 선택할 때 연속으로 2개의 요소 선택 불가능
# 식량을 최대화 하는 선택에서 식량의 개수



# Solution
# 배열이 arr[i]일때
# 각 arr[i]를 선택하는 경우와 선택하지 않는 경우 2가지가 존재
# dp table = dp[N][2]
# dp[i][0] : arr[i]를 선택하지 않는 경우 = max(dp[i-1][0], dp[i-1][1])
# dp[i][1] : arr[i]를 선택하는 경우 = dp[i-1][0] + arr[i]
# 정답 =>  max(dp[N-1][0], dp[N-1][1])

# 초기값
# dp[0][0] = 0
# dp[0][1] = arr[0]
def get_result(arr):
    
  N = len(arr)
  
  dp = [[0]*2 for _ in range(N)]
  
  # 초기값
  dp[0][1] = arr[0]
  
  for i in range(1,N):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    dp[i][1] = dp[i-1][0] + arr[i]

  return max(dp[N-1])



# f(n) : n일때 최대식량
# f(n-1) >= f(n-2) : 항상 성립
# f(n-1) == f(n-2) 인 경우 arr[n-1] 은 채택 x => 따라서 arr[n] 채택
# f(n-1) > f(n-2) 인 경우 arr[n-1] 은 채택 o  => 따라서 arr[n] 채택 불가능
# 점화식  : f(n) = max(f(n-1), f(n-2)+arr[n])
# Bottom-Up
def get_result2(arr):
          
  N = len(arr)
  arr.insert(0,0)
  
  
  dp = [0]*(N+1)
      
  # 초기값
  dp[1] = arr[1]
  
  for i in range(2,N+1):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])
    

  return dp[N]



def recursion(arr, i, memo):
  
  if i == 0 : return 0
  
  if i in memo : return memo[i]
    
  memo[i] = recursion(arr, i-1, memo)
  memo[i] = max(memo[i], recursion(arr, i-2, memo) + arr[i] )
    
  return memo[i]


# Top-Down
def get_result3(arr):
  
  N = len(arr)
  arr.insert(0,0)
  
  memo = { 1 : arr[1]}

  
  return recursion(arr, N, memo)
  
  
  
  
  
  
  
print(get_result([1,3,1,5]))

print(get_result2([1,3,1,5]))
print(get_result3([1,3,1,5]))