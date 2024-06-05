from algorithm.noc.combinations import combinations_with_duplication
from algorithm.noc.permutations import permutations_with_duplication
from itertools import combinations

items = ['B', 'B', 'C','A','A']


noc = sum(True for _ in combinations_with_duplication(items,3))
assert noc == len(set(combinations(items,3)))