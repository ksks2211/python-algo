from collections import Counter


def combinations_with_duplication(elements, n):
  
  elements.sort()  
  cnt = Counter(elements)
  items = list(cnt.keys())
  items_count = list(cnt.values())
  
  
  yield from _combinations_with_duplication(items, items_count, n, [], cnt.total())
  
def _combinations_with_duplication(items, count, n, cur, remaining_elements_count):
  
  if len(cur) == n : 
    yield tuple(cur[:])
    return
  
  
  k = len(items)
  
  for i in range(k):
    

    if count[i] > 0 :
      
      # pruning
      if len(cur) + remaining_elements_count < n : return    
    
      count[i] -=1
      remaining_elements_count-=1
      cur.append(items[i])
            
      yield from _combinations_with_duplication(items[i:], count[i:], n, cur, remaining_elements_count)
      
      remaining_elements_count-=count[i]      
      cur.pop()
      