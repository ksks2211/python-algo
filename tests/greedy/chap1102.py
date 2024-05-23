# Question
# (A) 숫자로 이뤄진 문자열 S, 1 <= len(S) <= 20
# (B) 숫자 사이에 x or  + 를 넣기
# (C) 연산은 수학연산과 달리 그냥 왼쪽 => 오른쪽 순서로 




# Solution
# 가장 왼쪽을 l
# for r in letters[1:] 
#   l x r, l + r 을 비교해서 큰것을 l로
#   l = max(l*r, l+r)  
# return l

def get_result(S):
    
  l = int(S[0])
    
  for r in S[1:]:
    r = int(r)
    l = max(l+r,l*r)

  return l





# Solution2
# n x m 과  n + m 을 비교 
# n x m - n - m  = (n - 1)(m - 1) - 1 = F

# F > 0 이면 n x m 이 더큼
# F == 0 이면 동일
# F < 0 이면 n + m 이 더큼

# (n + m)이 더 큰 경우
# n == 1 or m == 1  => -1
# n == 0  => -m (m==0인 경우엔 같음)
# m == 0 => -n (n==0인 경우엔 같음)
# 따라서 n <= 1 or m <= 1 일때만 더하기 연산을 하면 
# 결과값은 곱하기보다 크거나, 최소한 같음

# 복잡도 : O(N), N = len(S)

def get_result2(S):    
  l = int(S[0])    
  for r in S[1:]:
    r = int(r)    
    if l <= 1 or r <=1 :
      l = l+r
    else:
      l = l*r
  return l
 
 
print(get_result2('02984'))
print(get_result2('567'))
 