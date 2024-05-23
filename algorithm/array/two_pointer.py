





def count_interval_sum(arr:list[int], target:int):
  
  count = 0
  
  # start ~ end-1,  sum(arr[start:end])
  interval_sum = 0
  
  end = 0
  
  limit = len(arr)
  
  
  # Forward Start
  for start in range(limit):
    
    
    # Forward End 
    while interval_sum < target and end < limit:
      interval_sum += arr[end]
      end+=1
      
    
    # interval_sum >= target or  end == limit
    if interval_sum == target: count +=1      
    
    interval_sum -= arr[start]
  
  
  return count
  
  

def merge(arr1, arr2):
  
  n, m =  len(arr1), len(arr2)
  
  i = j = 0
    
  result = [0]*(n+m)
    
  while i < n or j < m:        
    if j>=m or (i < n and arr1[i] < arr2[j]):
      result[i+j] = arr1[i]
      i+=1
    else:
      result[i+j] = arr2[j]
      j+=1          
  
  return result    



def sums(arr, queries):
  
  
  
  current_sum = 0
  prefix_sum = [0]
  
  for value in arr:
    current_sum += value
    prefix_sum.append(current_sum)
  
  
  result = []
  # left <= i < right
  for (left, right) in queries :
    result.append(prefix_sum[right]-prefix_sum[left])
    
  return result    