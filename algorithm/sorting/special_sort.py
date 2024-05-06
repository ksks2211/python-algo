

def count_sort(arr):
  base = min(arr)
  count = [0]*(max(arr)-base+1)
  
  
  for el in arr:
    count[el-base]+=1
  
  result = [0]*len(arr)
  
  i = 0
  for v, cnt in enumerate(count):    
    el = v + base
    
    for _ in range(cnt):
      result[i] = el
      i+=1
  
  return result    
  