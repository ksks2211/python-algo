from algorithm.sorting import basic_sort, advanced_sort, special_sort
from algorithm.helper import sort_helper
import doctest
import time    

arr = list(sort_helper.random_integers(20000,5000))




doctest.testmod()
start = time.process_time()
# sorted_arr = basic_sort.selection_sort(arr)
sorted_arr = advanced_sort.merge_sort(arr)
# sorted_arr = special_sort.count_sort(arr)


print(f"Processing time: {(time.process_time() - start)%1e6} seconds")


assert sort_helper.is_sorted(sorted_arr), "Not Sorted!"


# quick sort : 0.0 ~ 0.03
# shell sort : 0.015 ~ 0.06
# heap sort : 0.0 ~ 0.015
# bubble sort : 2.4 ~ 2.8
# insertion sort : 1.0 ~ 1.6
# selection sort : 1.0 ~ 1.5