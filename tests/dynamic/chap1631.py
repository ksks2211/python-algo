# Question
# (A) n x m 크기의 금광 
# (B) 첫번째 열에서 출발(행은 아무거나)
# (C) 다음번 위치에서는 북동 동 남동 3방향 중 1개선택
# 채굴자가 얻을 수 있는 최대 금의 크기는?




# matrix[i][j] 

# S[i][j] : j열에서 i를 선택했을때의 최댓값
# S[i][j] = matrix[i][j] + max(S[i][j-1], S[i-1][j-1], S[i+1][j-1])

# i가 존재하는 지 체크     0 <= ni < N


# DP[j] : j열 에서 최댓값
# DP[j] : max(S[0][j], S[1][j], ..  S[i][j])


# 시간복잡도 O(nm)
def get_result(matrix, n, m):
  
  
  
  # from column 1 ~ m-1
  for j in range(1, m):    
    for i in range(n):      
      biggest = matrix[i][j-1]      
      if 0 <= i-1: 
        biggest = max(biggest, matrix[i-1][j-1])      
      if i+1 < n :
        biggest = max(biggest, matrix[i+1][j-1])
      matrix[i][j] += biggest             
        
  
  
  return max(row[m-1] for row in matrix)
    
    


matrix = [
  [1,3,3,2],
  [2,1,4,1],
  [0,6,4,7]
]
print(get_result(matrix, 3,4))


matrix = [
  [1,3,1,5],
  [2,2,4,1],
  [5,0,2,3],
  [0,6,1,2]
]

print(get_result(matrix, 4,4))
