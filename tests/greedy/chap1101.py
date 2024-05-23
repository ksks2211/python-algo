# Question
# (A) N명의 모험가 1 <= N <= 100,000
# (B) 각 모험가는 공포도 를 가짐  1 <= 공포도 <= N
# (C) 공포도가 X인 모험가는 X명 이상이 포함된 그룹이어야 모험가능
# (D) 모든 모험가가 모험을 떠날 필요는 없음, 남아있기 가능
# 그룹 개수의 최대값

# Solution
# 1. 공포도 숫자가 클수록 그룹형성이 어려움
# 2. 그룹 조건, Group = list(), max(group) <= len(group)
# 3. 오름차순 sorting해서 그룹에 추가하기
# 4. group의 조건을 만족하는 순간 바로 그룹으로 묶기
# 5. sorting 순서대로 그룹에 넣기 = 그룹형성이 쉬운 순서
# 그룹을 만족하는지 체크하는 validation 함수
# 각 모험가에 대해서 반복문을 돌면서 그룹을 만족하면 count 증가 + 그룹 초기화


# 시간복잡도
# sorting : O(nlogn) + O(n)

def validate(group):  
  if len(group) == 0 : return False
  
  if max(group) <= len(group) : return True
  
  return False

def get_result(levels):
  
  levels.sort()
  
  group = list()
  
  count = 0
  for member in levels:
    group.append(member)
    # group is made
    if validate(group):
      count +=1
      group = list()
      
  return count  



# Solution2
# 실제로 group 데이터를 유지할 필요 없음
# cur_group_size : 현재 그룹에 포함된 개수 
def get_result2(levels):
  levels.sort()
  
  count = 0
  cur_group_size = 0
  for member in levels:
    cur_group_size +=1 
    
    if cur_group_size >= member: 
      count +=1
      cur_group_size=0
  return count


print(get_result([2,3,1,2,2]))
print(get_result2([2,3,1,2,2]))

