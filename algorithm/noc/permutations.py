from collections import Counter



# Pick n elements
# n elements can have duplicated elements
def permutations_with_duplication(elements, n):
  
  cnt = Counter(elements)
  
  items = list(cnt.keys())
  items_counts = list(cnt.values())
      
  yield from _permutations_with_duplication(items, items_counts, n, [])
  

def _permutations_with_duplication(items, counts, n, cur):
    
  if len(cur) == n : yield tuple(cur[:])
    
  for i in range(len(items)):
    if counts[i] > 0 :
      counts[i]-=1
      cur.append(items[i])
      yield from _permutations_with_duplication(items, counts, n, cur)
      counts[i]+=1
      cur.pop()
  