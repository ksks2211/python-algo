# Question
# (A) '0' or '1' 로 이루어진 문자열 S가 주어짐
# (B) 연속된 숫자는 뒤집기 가능
# 최소한으로 뒤집어서 모두 같은 숫자로 맞출 때 횟수는



# Solution
def get_result(S):
  n = len(S)
  
  if n <= 1 : return 0
  
  a, b = 0, 0
  
  for i in range(1, n):
    if S[i]=='0' and S[i-1]=='1' : a+=1
    elif S[i]=='1' and S[i-1]=='0': b+=1
    
  if S[-1]=='0' : b+=1
  else : a +=1
  
  return min(a,b)


# Solution2
# 숫자를 압축하면 010101 = (101010) 같은 패턴
# 0부터 시작하는 경우만 고려
# (empty)  => 반전 0 회 => 0
# 0 => 반전 0회 => 0
# 01 => 반전 1회 => 1
# 010 => 반전 2회 => 1
# 0101 => 반전 3회 => 2
# 01010 => 반전 4회 => 2
# 패턴  (반전 횟수 + 1) // 2 
def get_result2(S):
  n = len(S)
  
  if n <= 1 : return 0
  
  cnt = 0
  for i in range(1, n):
    if S[i] != S[i-1]: cnt+=1

  return (cnt+1)//2


print(get_result("0001100"))