from algorithm.noc.permutations import permutations_with_duplication, next_permutation, prev_permutation
from itertools import permutations


duplicated_items = ['A','A','B','B','C']

noc = sum(True for _ in permutations_with_duplication(duplicated_items, 3))

assert noc == len(set(permutations(duplicated_items, 3)))






items = [0,0,0,1,1]


while True:
  
  print(items)
  has_next = next_permutation(items)
  
  if not has_next:break


print("=========")
while True:
  
  print(items)
  has_prev = prev_permutation(items)
  
  if not has_prev:break  