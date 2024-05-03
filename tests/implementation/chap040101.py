# Question
# (A) NxN 크기의 공간, (1,1)  (N,N) 좌표
# (B) 계획서를 따라 상하좌우 이동가능, 이동 불가능한 경우 무시
# (C) 출발점은 (1,1) 
# 도착점의 좌표를 출력





def get_result(n, directions):
  x,y = 1,1
  for dir in directions:
    
    if dir == 'L' and y > 1: y-=1
    elif dir =='R' and y < n : y+=1
    elif dir =='U' and x > 1 : x-=1
    elif dir == 'D' and x < n : x+=1
  
  return (x,y)
  
  
  
  
print(get_result(5, ['R','R','R','U','D','D']))
