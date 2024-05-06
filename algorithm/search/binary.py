def binary_search(arr, target):
    
  start, end = 0, len(arr)-1
  
  while start<=end:
    middle = (start+end)//2
    if arr[middle] == target : return middle
    elif arr[middle] < target : start = middle+1
    else : end = middle-1
  
  return -1


