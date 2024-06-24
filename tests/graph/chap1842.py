# Question
# (A) G개의 탑승구 1 <= G <= 100,000
# (B) P개의 비행기가 차례대로 도착
# (C) 비행기는 탑승구중 하나에 도킹
# (D) 도킹 불가능하면 => 공항 운행중지
# (E) 각 비행기는 gi 를 가짐
# (F) 비행기는 1 ~ gi 번째 탑승구중 하나에만 도킹 가능



# Solution
# 서로소 집합 알고리즘 사용
# 비행기가 gi를 가질때 gi에 가까운 큰 값일수록 좋음
# p = find(gi)
# 한 비행기가 p를 사용하는 경우
# (p, p-1) 을  p-1로 통합(union)
# union(1, 0) 이 발생하는 경우 불가능 





def get_result(G, P, schedule):
  
  
  pass

G = 4
P = 3
schedule = [4,1,1]

print(get_result(G,P, schedule))