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
  