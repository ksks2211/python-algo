# Question
# - N개의 수로 이루어진 수열, 2 <= N <= 11
# - N-1 개의 연산자
# - 연산은 우선순위를 무시하고 앞에서 부터
# - 나누기 : 몫만, 음수인경우 => 양수로 바꿔서 나누고 마이너스 처리
# => 결과 값의 최대값과 최소값 찾기

# Solution
# 나눗셈 =>  math.trunc(a/b)


# DFS 로 찾기 dfs(items, counter, sm, lg) => (min, max)
# items는 immutable , counter는 mutable 




import math

MAX_NUM = float('infinity')
MIN_NUM = -MAX_NUM

def dfs(items, counter, sm=MAX_NUM, lg = MIN_NUM):  
  if len(items)==1 :    
    sm = min(sm, items[0])
    lg = max(lg, items[0])    
    return (sm, lg)
  
  
  for i in range(4):    
    if counter[i] == 0 : continue
    
    counter[i]-=1
    
    
    result = items[0]
    if i == 0 : result+=items[1]
    elif i==1 :  result-=items[1]
    elif i==2 : result*=items[1]
    else : result = math.trunc(result/items[1])
      

    n_sm , n_lg = dfs([result, *items[2:]], counter, sm, lg)
    sm = min(sm, n_sm)
    lg = max(lg, n_lg)
    counter[i]+=1  
    
  
  
  return (sm,lg)





# DFS 효율화 dfs(front, cur_idx, items, )



def get_result(items, counter):  

  # Mutable
  sm_lg = [MAX_NUM, MIN_NUM] 
  
  # Immutable
  N = len(items)
  
  def dfs2(front, rear_idx):
    
    if rear_idx == N :
      sm_lg[0] = min(sm_lg[0], front)
      sm_lg[1] = max(sm_lg[1], front)
      
      return
    
    for i in range(4):
      if counter[i] == 0 : continue
      
      counter[i]-=1
      
      result = front
      
      if i == 0 : result += items[rear_idx]
      elif i == 1 : result -= items[rear_idx]
      elif i == 2 : result*=items[rear_idx]
      else : result = math.trunc(result/items[rear_idx])
            
      dfs2(result, rear_idx+1)    
                  
      counter[i]+=1
  
  
  dfs2(items[0], 1)            
  return tuple(sm_lg)
  
  
    
    
  





print(get_result([5,6],[0,0,1,0]))
print(get_result([3,4,5],[1,0,1,0]))

print(get_result([1,2,3,4,5,6],[2,1,1,1]))