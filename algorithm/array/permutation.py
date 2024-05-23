


def next_permutation(arr):
  
  n = len(arr)
  
  
  # find largest i satisfies a[i-1] < a[i]  
  i = n-1  
  while i > 0 and arr[i-1] >= arr[i] : i-=1    
  if i == 0 : return False
  
  
  # find largest j satisfies a[i-1] < a[j]
  # always exists because a[i-1] < a[i]
  j = n-1  
  while arr[i-1] >= arr[j] : j-=1
  
  
  # swap i-1 and j
  arr[i-1], arr[j] = arr[j], arr[i-1]
  
  
  
  # reverse arr[i:]
  start = i
  end = n-1
  
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start+=1
    end-=1
  
  return True


def prev_permutation(arr):
  n = len(arr)
  
  i = n-1  
  while i > 0 and arr[i-1] <= arr[i] : i-=1  
  if i==0 : return False
  
  
  j = n-1
  while arr[i-1] <= arr[j] : j-=1
  arr[i-1],arr[j]= arr[j], arr[i-1]
  
  
  start =  i
  end = n-1
  
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start+=1
    end-=1
  return True    