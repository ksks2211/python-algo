



def hanoi_count2(disk_count):
  return 2**disk_count - 1

def hanoi_count(disk_count):
  if disk_count == 1 : return 1    
  return 2 * hanoi_count(disk_count-1) + 1



def hanoi_find_movement(disk_count:int, col_from:int, col_to:int):
  
  if disk_count == 0 : return 
  
  
  col_middle = 6 - col_from - col_to
  
  yield from hanoi_find_movement(disk_count-1, col_from, col_middle)
    
  yield (disk_count, col_from, col_to)
  
  yield from hanoi_find_movement(disk_count-1, col_middle, col_to)
