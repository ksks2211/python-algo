from bisect import bisect_left, bisect_right

def binary_search(arr, target):
    
  start, end = 0, len(arr)-1
  
  while start<=end:
    middle = (start+end)//2
    if arr[middle] == target : return middle
    elif arr[middle] < target : start = middle+1
    else : end = middle-1
  
  return -1


def binary_search2(arr, target):
  i = bisect_left(arr,target)
    
  if i != len(arr) and arr[i]==target : return i  
  else : return -1

def count_elements(arr, element)  :
  return bisect_right(arr,element) - bisect_left(arr,element)