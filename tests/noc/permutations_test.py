from algorithm.noc.permutations import permutations_with_duplication
from itertools import permutations


duplicated_items = ['A','A','B','B','C']

noc = sum(True for _ in permutations_with_duplication(duplicated_items, 3))

assert noc == len(set(permutations(duplicated_items, 3)))
