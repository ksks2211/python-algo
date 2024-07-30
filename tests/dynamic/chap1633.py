# Question
# - N+1 번째 되는날 퇴사
# - 상담 : 상담 시작 날짜 + 상담 기간 + 상담 보상액



# Solution
# - 상담 [(start, t, p), ...  ]일때
# max_profit = [0,0,0,0,....] 으로 초기화
# 각 상담에 대해서 반복문 
# 상담을 하지 않는 경우 기대되는 최대수익과 비교 (어제의 최대수익 vs. 알려진 최대수익)
#   max_profit[start] = max(max_profit[start-1], max_profit[start])
# 상담을 하는 경우 기대되는 수익으로 비교
#   max_profit[start + t - 1] = max(max_profit[start + t - 1], max_profit[start-1] + p)





def get_result(N, plans):
      
  max_profit = [0]*(N+1)
    
  for i, (t, p) in enumerate(plans, 1):    
    max_profit[i] = max(max_profit[i-1], max_profit[i])    
    if i+t-1 <= N :
      max_profit[i+t-1] = max(max_profit[i+t-1], max_profit[i-1] + p)
      
  
  return max_profit[N]



N = 7
plans = [(3,10),(5,20),(1,10),(1,20),(2,15),(4,40),(2,200)]
print(get_result(N, plans))


N = 10
plans = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10)]
print(get_result(N, plans))

    
N = 10
plans = [(5,10),(5,9),(5,8),(5,7),(5,6),(5,10),(5,9),(5,8),(5,7),(5,6)]
print(get_result(N, plans))


N=10
plans = [(5,50),(4,40),(3,30),(2,20),(1,10),(1,10),(2,20),(3,30),(4,40),(5,50)]
print(get_result(N, plans))

  





