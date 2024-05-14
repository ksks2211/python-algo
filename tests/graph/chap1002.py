# Question
# (A) 0~N 까지의 N-1개의 팀
# (B) 팀 union = 0 , find = 1 연산 사용가능
# (C) M개의 연산(union or find) 사용
# find 연산결과 같으면 YES display 아니면 No display






def find(parent, x):
  if parent[x]!=x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a, b = find(parent,a), find(parent,b)
  
  # if a==b : raise Exception("Cycle detected!") 
  
  if a < b : 
    parent[b] = a
  else :
    parent[a] = b
  

def get_result(n, commands):
  
  parent = [i for i in range(n+1)]
  
  
  for flag, a,b in commands:
    if flag==0:
      union(parent, a,b )
    else:
      ap = find(parent,a)
      bp = find(parent,b)
      
      if ap==bp : print("YES")
      else : print("NO")
      


get_result(7, [(0,1,3),(1,1,7),(0,7,6),(1,7,1),(0,3,7),(0,4,2),(0,1,1),(1,1,1)])  
  
  