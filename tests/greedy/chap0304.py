# Question
# (A) N과 K가 주어진다 2 <=   K<=N  <=100,000  
# (B) N을 1로 만드는 것이 목표
# (C) N에서 1을 빼거나, N을 K로 나눈 몫을 N으로(나누어 떨어지는 경우에만) 연산
# (D) 연산 횟수를 최소화
# N을 1로 만들때의 연산 횟수

# Solution
# - 나누기 연산이 불가능한 경우 => 뺄셈만 가능
# - 나누기 연산이 가능한 경우 : N = K*M 일때  M-1 까지 걸리는 횟수 (M > 1)
#   - 나누는 경우 : K*M => M => M-1   (2회)
#   - 빼는 경우 : K*M => K*M - K => M-1  (K+1회)
#   - 항상 나누는 것이 유리
# - 나누기 연산이 가능하고 N = K 일때  (M=1)
#   - 나누는 경우 : K => 1 (1회)
#   - 빼는 경우 : K => 1 (K-1회)
#   - 2<=K 이므로 항상 나누는 것이 같거나 유리
# 결론 : 나누기가 가능하면 항상 나누기


# 시간복잡도 : O(N-K)

def get_result(n,k):
  
  count = 0
  
  while n !=1:
    share, remain = divmod(n, k)
                
    # 뺄셈 (나누어 떨어지지 않는 경우)
    if remain !=0 : 
      n-=remain
      count += remain
    # 나눗셈      
    else:
      n = share  
      count+=1  
  return count


print()
print(get_result(25,5))