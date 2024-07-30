# Question
# - N명의 병사가 나열
# - 병사 : 번호 + 전투력
# - 전투력 내림차순으로 배치
# - 배치를 위해서 원래 순서에서 일부 병사 제외시키기
# - 조건(내림차순)을 만족하면서 남아있는 병사가 최대가 되도록 함
# - 제외시킬 최소 병사의 수 출력

# Solution 
# - 계산을 위해서 idx=0 을 추가   power[0]=0
# - table[i] : 0 ~ i번째 병사를 고려할때, 최소 병사의 수
# 점화식
# - table[0] = 0
# - table[1] = 0
# - table[i]
# power[i-1] > power[i] 인 경우 : table[i] = table[i-1]
# power[i-1] == power[i] 인 경우 : table[i] = table[i-1] + 1 (버리기와 같음)
# power[i-1] < power[i] 인 경우 : 
#     i번째를 버리는 경우 table[i] = table[i-1] + 1
#     i번째를 포함하는 경우 
#     power[j] > power[i]  인 j를 찾기 
#     table[j] + i - j + 1
#     max(table[i-1]+1, table[j] + i - j + 1)


def get_result(N, powers):
      
  table = [1] * N  
  
  result = 1
  
  for i in range(1,N):    
    for j in range(0,i):
      if powers[i] < powers[j] and table[i] < table[j]+1:
        table[i] = table[j] + 1    
        
    result = max(result, table[i])
 
 
  return N - result


print(get_result(7,[15,11,4,8,5,2,4]))
