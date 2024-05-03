# Question
# (A) 8x8 행렬
# (B) L자 형태로 이동 
# (C) 행(1~8), 열(a~h)


# Solution
# 이동 경로 : 최소 2개 최대 8개




def checker(x,y):
  if 1 <=x <=8 and 1<=y<=8 : return True
  return False
  


def get_result(position):  
  
  dx = [2,2,-2,-2,1,1,-1,-1]
  dy = [1,-1,1,-1,2,-2,2,-2]
  
  
  col = ord(position[0]) - ord('a') + 1
  row = int(position[1])
    
  cnt = 0
  for i in range(8):
    nx,ny = row+dx[i], col+dy[i]
    if checker(nx,ny) : cnt+=1
  return cnt    
    

print(get_result('a1')  )
  


