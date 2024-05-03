# Question
# (A) N,M 크기의 Map
# (B) 1=바다 0=육지
# (C) 방향  북(N=0), 동(E=1), 남(S=2), 서(W=3)
# (D) 현재방향의 반시계 방향 순서로 탐색
# (E) 왼쪽으로 회전 
#   - 육지 or 미방문 칸이면 전진후 방문
#   - 육지 or 미방문 칸이면 주변 4방향에 
# 



# Solution
# 0 - dir(현재방향), cnt(방문한 칸의 수), position(캐릭터 위치)
# 1 - 현재좌표+현재방향을 입력받아 4방중 이동가능한 곳이 있는지 체크하고 존재하면 방향과 위치, 없으면 null,  check_movable
# 2 - 현재방향을 입력하면 그 왼쪽방향을 출력하는 함수  rotate_dir
# 3 - 현재방향을 입력하면 그 반대방향을 출력하는 함수  across_dir
# 4 - 현재좌표와 방향을 입력하면 다음좌표를 출력하는 함수 get_next
# 5 - 종료조건 : 1이 False 이면서, 뒷칸이 바다(=1)


dirs = {
  0 : (-1,0),
  1 : (0,1),
  2 : (1,0),
  3 : (0,-1)
}

def rotate_dir(dir):
  dir-=1
  if dir<0 : dir=3
  return dir

def backward_dir(dir):
  dir = rotate_dir(dir)
  return rotate_dir(dir)
  
def get_next(cur, dir):
  x,y = cur
  dx,dy = dirs[dir]  
  return (x+dx, y+dy)


# map의 외곽은 항상 바다 + 육지에서 출발 이라는 조건 존재 == 생략가능
def validate(x,y, n, m):
  if 0<=x<n and 0<=y<m : return True
  return False


def check_movable(n,m , map, cur,dir):    
  for _ in range(4):
    
    # rotate left
    dir = rotate_dir(dir)
    
    # next position
    nx, ny = get_next(cur,dir)
    
    # next position is valid and not visited,  validate(nx,ny, n,m) 생략
    if map[nx][ny] == 0: 
      
      # mark visit 
      map[nx][ny] = 2
      
      # new position, direction
      return ((nx,ny), dir)  
  return None 

def get_result(n,m, map, cur, dir):
  
  x,y = cur
  
  # visit start point 
  map[x][y] = 2
  cnt = 1
  
  
  while True:
    result = check_movable(n,m, map, cur, dir)    
    if result != None :       
      cur, dir = result      
      # visit      
      cnt += 1
    else:      
      opposite_dir = backward_dir(dir)
            
      cur = get_next(cur, opposite_dir)
      x,y = cur
      if map[x][y]==1 :break
      
  return cnt
  
  
  
map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]] 
  
print(get_result(4,4,map, (1,1),0))