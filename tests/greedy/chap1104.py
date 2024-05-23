# Question
# (A) N개의 동전 (액수 같은 동전 여러개 가능)
# (B) 동전의 개수 1 <= N <= 1,000
# 동전을 사용해서 만들수 없는 양의 정수 금액의 최소값



# Solution
# 동전을 sort => coins.sort()
# 동전은 쓴다 or 안쓴다 두가지 선택지
# coins[:i] 의 조합가능 범위가 0 ~ a 라고 가정하면
# coins[i+1] = b  에 의해 추가로 가능해지는 범위는   b ~ a+b     
#  b <= a+1 이라면 coins[:i+1] => 0 ~ a+b 
#  b > a+1 이라면  a+1 부터 제작 불가능

# coins[0] != 1 => return 1
# else 
#   coins[:0] => 0 ~ 1

def get_result(coins):  
  coins.sort()
  a = coins[0]  
  if a != 1 : return 1
  
  for b in coins[1:]:
    if b <= a+1: a+=b
    else: break
   
  return a+1    
  

# 0 ~ target - 1 까지의  조합 생성가능하다고 가정
# coins[i] = value 일때 => value ~ target + value - 1 까지 가능
# value <= target 이라면 => 0 ~ target + value - 1  까지 가능
# value > target 이라면 => target ~ value - 1 까지는 불가능 => target 이 가장 작은값
# 찾는것은 조합 자체가 아니라 범위



# coins[i] 에서 불가능으로 나온 범위는
# coins[i+1] 에서도 불가능 



# 시간복잡도 : 정렬 O(nlogn)
# 반복문 : O(n)
def get_result2(coins):
  coins.sort()
  
  target = 1
  
  for value in coins:
    if value > target : break
    else : target += value
  
  return target
  
  
print(get_result2([3,2,1,1,9]))  
  
# 이때까지 나온 숫자들의 총합이, 새로운 숫자-1 보다 작은 경우 => return cur_sum + 1
def get_result3(coins):
  coins.sort()
  cur_sum = 0
  
  for value in coins:
    if cur_sum < value - 1 : break
    else : cur_sum+=value
  return cur_sum+1    