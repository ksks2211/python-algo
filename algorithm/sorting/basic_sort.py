from typing import Any

def bubble_sort(arr:list[Any]) -> list[Any]:  
  arr = arr[:]  
  for i in range(len(arr)):
    is_sorted = True    
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1],arr[j]
        is_sorted=False    
    if is_sorted : break
  return arr




# python -m algorithm.sorting.basic_sort
if __name__ == "__main__":
  import doctest
  import time    
  from ..helper.sort_helper import is_sorted, random_integers
  
  
  doctest.testmod()
  arr = list(random_integers(20,10))
  
  start = time.process_time()
  bubble_sort(arr,inplace=True)    
  print(*arr,sep=",")
  print(f"Processing time: {(time.process_time() - start)%1e9 + 7}")
  assert is_sorted(arr)
  
  