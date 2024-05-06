# Question
# (A) N개의 떡, 1 <= N <= 1,000,000
# (B) 최소 M길이의 떡, 1<= M <= 2,000,000,000
# (C) 절단기 설정 높이의 최댓값

# Solution
# 떡의 높이 배열 : arr
# 절단기 설정 높이의 최솟값 : 0 
# 절단기 설정 높이의 최댓값 : max(arr)
# Parametric search


# 시간복잡도
# 가장 큰 수가 n 일때 => O(log n)

def get_sum(arr,h):  
  return sum(map(lambda e: 0 if e<=h else e-h, arr))


def get_result(arr, m):
  
  start, end = 0, max(arr)
  
  result = 0
  while start <= end : 
    h = (start+end)//2 
    if get_sum(arr,h)>=m : 
      result = h
      start = h+1
    else:
      end = h-1
        
  return result


print(get_result([19,15,10,17],6))