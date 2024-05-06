# Question
# (A) N개의 자연수로 구성된 2개의 배열 A, B
# (B) 바꾸기 : A원소와 B원소 하나씩을 바꾸는 연산 가능
# (C) 바꾸기 K번 까지가능, 항상 0 <=  K <= N
# A 배열의 원소합이 최대가 되게 


# Solution
# A는 오름차순 정렬
# B는 내림차순 정렬
# i = 0 ~ min(k,n)-1 => C 조건에 의해 0 ~ k-1
#   B[i] > A[i] 이면 교환 = i++
#   B[i] <= A[i]  이면 중단
# A 배열의 합 리턴

# 시간복잡도 : O(nlogn) - 정렬 


def get_result(A, B, n, k):

  A.sort()
  B.sort(reverse=True)
  
  for i in range(k):
    if A[i] < B[i] : 
      A[i],B[i] = B[i],A[i]
    else : break
    
  return sum(A)          



print(get_result([1,2,5,4,3],[5,5,6,6,5],5,3))

  
