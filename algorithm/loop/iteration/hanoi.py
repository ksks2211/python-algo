def hanoi_count(disk_count):
  if disk_count == 1 : return 1    
  
  count = 1
  
  for _ in range(2, disk_count+1):
    count = count*2 + 1
  return count    