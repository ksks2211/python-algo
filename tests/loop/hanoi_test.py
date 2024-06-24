from algorithm.loop.recursion.hanoi import hanoi_find_movement, hanoi_count, hanoi_count2



for (plate, col_from, col_to) in hanoi_find_movement(3,1,3):
  
  print(f'{plate} 원판 : {col_from}기둥 => {col_to}기둥')


assert hanoi_count(3) == hanoi_count2(3)