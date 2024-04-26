# Question
# (A) 가장 높은 수가 적힌 카드를 뽑는 게임
# (B) N행 M열로 놓인 카드, 1<= N,M <=100
# (C) 카드의 숫자는 1~10,000
# (D) 행을 선택해서 해당 행의 가장 낮은 수가 뽑힘
# 게임의 룰을 만족하면서 카드를 뽑을 때 뽑힌 수


# Solution
# 행별로 가장 작은 수 찾기
# 가장 작은 수 중에서 큰 것 찾기

# 시간 복잡도
# 행별로 정렬 O(N M logM)
# 열별로 정렬 O(N logN)



def get_result(matrix):  
  arr = list(map(lambda row: min(row), matrix))  
  return max(arr)



matrix = [[3,1,4],[4,1,4],[2,2,2]]


print(get_result(matrix))

matrix=[[7,3,1,8],[3,3,3,4]]
print(get_result(matrix))
