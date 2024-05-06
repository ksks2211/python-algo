import heapq


def gap_insertion_sort(arr, gap, n):  
  for i in range(gap, n):
    key = arr[i]    
    j = i - gap        
    while j >= 0 and arr[j] > key:
      arr[j+gap] = arr[j]
      j-=gap
    arr[j+gap]  = key
  return arr


def shell_sort(arr):
  arr=arr[:]
  n = len(arr)
  
  gap = n//2
  
  while gap > 0 :    
    gap_insertion_sort(arr, gap, n)
    gap = gap//2
  return arr    
    

def heap_pop(arr):
  while arr:
    yield heapq.heappop(arr)


def heap_sort(arr):
  arr= arr[:]
  heapq.heapify(arr)    
  return list(heap_pop(arr))
  

def quick_sort(arr):    
  if len(arr) <= 1 : return arr
  
  else:
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [ x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left)+middle+quick_sort(right)
  
