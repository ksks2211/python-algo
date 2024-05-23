# Question
# (A) 현재의 점수는 자릿수가 짝수인 N
# (B) 숫자를 반으로 쪼개서 각 자리수 합해서 같으면 lucky straight


def get_result(score):
  
  score = [int(score) for score in list(score)]
  
  mid = len(score) // 2
  
  
  
  if sum(score[:mid]) == sum(score[mid:]): return "LUCKY"
  else: return "READY"
  
  
assert get_result("123402")=='LUCKY'
assert get_result("7755")=='READY'