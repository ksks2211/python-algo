

def bubble_sort(arr, inplace=True):  
  arr = arr if inplace is True else arr[:]  
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
  
  from ..helper.sort_helper import is_sorted, random_integers
  
  arr = list(random_integers(20,10))
  
  bubble_sort(arr,inplace=True)  
  assert is_sorted(arr)
  print(arr)
  
  