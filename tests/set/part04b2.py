# Question
# (A) K개의 서로다른 소문자 알파벳에서 n개를 뽑을때
# (B) 조합은 최소 한개의 모음, 최소 한개의 자음을 만족해야 한다
from itertools import combinations


def validate(combination, n):
  vowels = set(['a','e','i','o','u'])
    
  count_vowels = sum(map(lambda x:x in vowels, combination))  
  if count_vowels >= 1 and n >= 2 + count_vowels : return True
  
  return False

def get_combination(letters, n):
  letters.sort()
  for c in combinations(letters, n):
    if validate(c, n) :
      yield c


letters = ['a','t','c','i','s','w']

for c in get_combination(letters,4):
  print("".join(c))





