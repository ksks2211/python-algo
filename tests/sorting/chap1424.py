# Question
# (A) 일직선상에 위치한 N개의 집(서로 같은 위치도 가능)
# (B) 집이 위치한 곳중 하나에 안테나를 설치
# (C) 안테나 - 각 집까지의 거리를 최소화
# (D) 안테나를 설치할 수 있는 곳이 여러개 있는경우 => 작은 것


# Solution
# e.g. 1 5 7 9  
# 1 => 0 4 6 8 => 18
# 5 => 4 0 2 4 => 10 == 18 +4x1 -4x3
# 7 => 6 2 0 2 => 10 == 10 +2x2 -2x2
# 9 => 8 3 2 9 => 13 == 10 +2x1 -2x3

#  a => b(=a+1) 의 거리가 n일때
# 안테나를 a에서 b로 옮기면
#  0 ~ a 번째 까지는 각각 n만큼 증가
#  b ~ 마지막 까지는 각각 n만큼 감소


def get_result(homes):
  
  homes.sort()
  
  n = len(homes)
  return homes[(n-1)//2]
  
  
  
  
print(get_result([5,1,7,9]))