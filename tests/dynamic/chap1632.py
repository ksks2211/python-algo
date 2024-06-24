# Question
# 1 - 2 - 3 - 4 - ... - n 개의 정수가 삼각형으로
# 꼭대기 에서 시작해서 내려옴, 대각선 오른쪽 or 왼쪽
# 내려올때는 
# 합이 최대가 되게 하는 수


# Solution
# dp[i][j] : 높이가 i 일때 pyramid[i][j]를 포함할때 최대값
# dp[i][j] = 
#   pyramid[i][j] + max(dp[i-1][j]+dp[i-1][j-1])  중간요소
#   pyramid[i][0] + dp[i-1][0]  시작요소
#   pyramid[i][m] + dp[i-1][m-1]  마지막요소

# biggest = max(dp[i][:])

def get_result(pyramid, height):
  
  
  for i in range(1, height):        
    for j in range(i+1):
      if j == 0 : pyramid[i][j] += pyramid[i-1][j]
      elif j==i : pyramid[i][j]+= pyramid[i-1][j-1]
      else : pyramid[i][j]+=max(pyramid[i-1][j], pyramid[i-1][j-1])
                    
  return max(pyramid[height-1])


pyramid = [
  [7],
  [3,8],
  [8,1,0],
  [2,7,4,4],
  [4,5,2,6,5]
]


print(get_result(pyramid, 5))


