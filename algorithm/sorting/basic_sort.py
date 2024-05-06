from typing import Any

def bubble_sort(arr:list[Any]) -> list[Any]:  
  arr = arr[:]  
  n = len(arr)
    
  for i in range(n):
    swapped = False
    
    # The last i elements are in place.
    for j in range(n-i-1):
      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1],arr[j]
        swapped=True    

    # If no two elements were swapped by inner loop, that means arr is sorted.
    if not swapped : break
  return arr

def insertion_sort(arr):
  arr=arr[:]
  n = len(arr)
  
  for i in range(1,n):
    key = arr[i]
    
    j = i - 1 
    
    # Move elements of arr[0..i-1], that are greater than key,
    # to one position ahead of their current position
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = key
  return arr    

def selection_sort(arr):  
  arr = arr[:]
  n = len(arr)
  
  for i in range(n-1):    
    min_idx = i
    
    # Find the minimum element in the remaining unsorted array
    for j in range(i+1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr    
      
