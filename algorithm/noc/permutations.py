from collections import Counter

# Pick n elements
# n elements can have duplicated elements
def permutations_with_duplication(elements, n):
  
  elements.sort()
  cnt = Counter(elements)
      
  items = list(cnt.keys())
  items_count = list(cnt.values()) 
        
  yield from _permutations_with_duplication(items, items_count, n, [], cnt.total())
  

def _permutations_with_duplication(items, count, n, cur, remaining_elements_count):
    
  if len(cur) == n : 
    yield tuple(cur[:])
    return
  
  # pruning
  if len(cur) + remaining_elements_count < n : return
    
  for i in range(len(items)):
    if count[i] > 0 :
      count[i]-=1
      cur.append(items[i])
      yield from _permutations_with_duplication(items, count, n, cur, remaining_elements_count-1)
      count[i]+=1
      cur.pop()




def next_permutation(items):
      
  N = len(items)    
  if N == 1 : return False
  
  
  i = N - 1 
  
  while i > 0 and items[i-1]>=items[i] : i-=1
  
  
  # End of permutation
  if i == 0 : return False
  
  j = N-1  
  while  items[i-1]>=items[j] : j-=1
  
  
  
  # Swap
  items[i-1],items[j] = items[j],items[i-1]
  
  
  start, end = i, N-1
  
  while start < end:
    items[start],items[end] = items[end],items[start]
    start+=1
    end-=1
  
  
  return True
  




def prev_permutation(items):
  N = len(items)
  if N == 1 : return False
  
  
  i = N-1
  
  while i > 0 and items[i-1]<=items[i]:i-=1
  
  if i == 0 : return False
  
  j = N-1
  while items[i-1] <= items[j]:j-=1
  
  # Swap
  items[i-1],items[j] = items[j],items[i-1]

  start, end = i, N-1
  
  while start < end:
    items[start],items[end] = items[end],items[start]
    start+=1
    end-=1

  return True      
  