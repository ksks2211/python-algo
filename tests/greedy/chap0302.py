# Question
# (A) 크기가 N인 배열
# (B) 배열에 있는 수를 M번 더해서 가장 큰 수를 만든다
# (C) 배열의 특정 인덱스의 수를 K번을 초과하여 (연속으로) 더할 수 없음
# (2 <= N <= 1000)
# (1 <= M <=10000)
# (1 <= K <=10000)


# Solution
# 배열을 내림차순으로 정렬
# 가장 큰 수를 K-1 번 사용 (N1, N2, ...)
# 두 번째로 큰 수를 1개 사용하고 다시 가장 큰 수를 K-1 번 사용하기 반복
# M >= K 인 경우    result += (N1 * K-1 + N2)  *  (M // K)   ,   M = M%K
# 0 < M < K 인 경우  result += (N1 * M)


# 시간복잡도 : O(1)

def get_result(m,k,arr):
  
  numbers = sorted(arr,reverse=True)  
  n1, n2 = numbers[0], numbers[1]
  
  
  share, remain = divmod(m, k+1)  
  
  n1_count = share * k
  n1_count += remain
  
      
  return n1_count*n1 + n2*(m-n1_count)
  
  
  
  
  
  


print(get_result(8,3,[2,4,5,4,6]))

# assert get_result(5,8,3,[2,4,5,4,6]) == 46, "Unexpected Result"