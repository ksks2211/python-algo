# Question
# (A) Fixed Point : 수열의 원소 중에서 값이 인덱스와 동일한 점
# (B) 서로다른 N개의 정수가 크기순으로 주어질 때, Fixed Point 찾기
# (C) 수열에 고정점이 존재하는 경우 => 출력
# (D) 수열에 고정점이 존재하지 않는 경우 => -1




# Solution
# Binary Search를 이용
# mid = (start + end)//2
# 고정점이 여러개라면? => left_most, right_most를 고려하기


# 시간복잡도 O(log N)  binary search

def find_left(arr):
  
  start, end = 0 , len(arr)-1
      
  idx = -1
  while start <= end:
    
    mid = start + (end - start)//2
    
    if mid == arr[mid] : 
      idx = mid

      
    if mid > arr[mid]:
      start = mid+1
    elif mid <= arr[mid]:
      end = mid-1
        
  return idx
  


def find_right(arr):
  start, end = 0 , len(arr)-1
      
  idx = -1
  while start <= end:
    
    mid = start + (end - start)//2
    
    if mid == arr[mid] : 
      idx = mid

      
    if mid >= arr[mid]:
      start = mid+1
    elif mid < arr[mid]:
      end = mid-1
        
  return idx

def get_result(arr):
  
  l = find_left(arr)
  

  
  if l == -1 : return -1
  r = find_right(arr)
  
        
  return tuple(arr[l:r+1])



arr = [-15, -6,1,3,7]
print(get_result(arr))

arr = [-15,-4,2,8,9,13,15]
print(get_result(arr))


arr = [-15,-4,3,8,9,13,15]
print(get_result(arr))


arr = [-1,1,2,3,4,5,9]
print(get_result(arr))