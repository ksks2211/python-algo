# Question
# (A) N명의 이름과 3과목 성적이 주어짐 
# (B) 이름을 정렬
# (C) 국어점수 내림 > 영어점수 오름 > 수학점수 내림 > 이름순


from functools import cmp_to_key

def compare(x,y):
  if x[1]!=y[1]:
    return y[1]-x[1]
  
  if x[2]!=y[2]:
    return x[2]-y[2]
  
  if x[3]!=y[3]:
    return y[3]-x[3]
  
  if x[0] < y[0]: return -1
  
  return 1
  
  

def get_result(students):
  
  key = cmp_to_key(compare)
  
  students.sort(key=key)
    
  return map(lambda s : s[0], students)



students = [
  ("Junkyu", 50, 60, 100),
  
  ("Sangkeun", 80, 60, 50),
  
  ("Sunyoung", 80, 70, 100),
  
  ("Soong", 50, 60, 90),
  ("Haebin", 50, 60, 100),
  ("Kangsoo", 60, 80, 100),
  ("Donghyuk", 80, 60, 100),
  ("Sei", 70, 70, 70),
  ("Wonseob", 70, 70, 90),
  ("Sanghyun", 70, 70, 80),
  ("nsj", 80, 80, 80),
  ("Taewhan", 50, 60, 90)
  ]



for student in get_result(students):
  
  print(student)