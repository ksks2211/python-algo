# Question
# (A) N x N 크기의 보드, 2 <= N <= 100
# (B) 사과의 개수 K 
# (C) 뱀이 벽 or 자신의 몸과 부딛히면 게임종료
# (D) 뱀은 매초 이동해야 함
# (D) 사과를 먹으면 뱀의 길이 증가
# (F) 다음칸에 사과가 있으면 꼬리유지 (=길이 증가)
# (G) 다음칸에 사과가 없다면 꼬리도 이동 (=길이 유지)
# (E) 시작위차 0,0   시작길이1  시작방향:오른쪽
# (H) 뱀은 90도씩 좌L or 우D 회전가능
#  게임이 끝나는 시간 출력

# Solution
# Head를 옮기기 전에 할 일
#   
#   증가된초에 방향이 변하는지 체크
#   이동가능 체크(벽아님 + 자신의 몸 아님)
#   이동방향 기록(나중에 꼬리도 옮겨야 하니까)
#   Tail은 사과가 있으면 그대로, 사과가 없으면 옮기기

#   초를 증가시키기
# Head를 옮기기

# 시간 + 방향을 담을 자료구조  deque()
# Map : -1 = 빈칸, 0~3 = 방향기록,  사과 = -2
# dirs = [ ... ]
# left(), right()
# next_point(cur_point, dir : 1~4)



from collections import deque
# right, down left, up
dirs = [(0,1),(1,0),(0,-1),(-1,0)]




def get_matrix(N, apples):  
  matrix = [[-1]*(N+1) for _ in range(N+1)]
    
  for i,j in apples:
    matrix[i][j] = -2
  
  return matrix
  


def validate(point, N, matrix):
  x, y = point
  
  if 1 <= x <= N and 1 <= y <=N and matrix[x][y] < 0 : return True
  return False
  
  
def left_rotate(dir):
  return (dir - 1 + 4) % 4

def right_rotate(dir):
  return (dir+1)%4
  



def move_point(cur_point, dir):
  cur_point[0] +=dirs[dir][0]
  cur_point[1] +=dirs[dir][1]
  



def get_result(N, apples, moves):
      
  matrix = get_matrix(N, apples)
  moves = deque(moves)
  
  head = [1,1]
  tail = [1,1]
  time = 0
  dir = 0
  
  while True:
    # decide direction
    if moves and moves[0][0] == time : 
      d_or_l = moves.popleft()[1]      
      if d_or_l == 'd' : dir = right_rotate(dir)
      else : dir = left_rotate(dir)
    
    # take time
    time += 1  
    
    # old point
    ox, oy = head  
        
    # move head and check if valid
    move_point(head, dir)    
    if not validate(head,N,matrix) : 
      break
      

    
    # remember direction 
    matrix[ox][oy] = dir

    # new point       
    nx, ny = head  
            
    # if not apple, move tail
    if not matrix[nx][ny] == -2 :      
      x, y = tail
      move_point(tail, matrix[x][y])      
      matrix[x][y]  = -1  # remove old tail

              
  return time
  
  
N = 6
apples = [(3,4),(2,5),(5,3)]
moves = [(3,'d'),(15,'l'),(17,'d')]
  
print(get_result(N, apples, moves))

N = 10
apples = [(1,2),(1,3),(1,4),(1,5)]
moves = [(8,'d'),(10,'d'),(11,'d'),(13,'l')]

print(get_result(N, apples, moves))


N = 10
apples = [(1,5),(1,3),(1,2),(1,6),(1,7)]
moves = [(8,'d'),(10,'d'),(11,'d'),(13,'l')]

print(get_result(N, apples, moves))
