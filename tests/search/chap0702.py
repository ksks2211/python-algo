# Question
# (A) 부품 1 <= N <= 1,000,000  N개, 부품엔 고유 부품번호 존재
# (B) 부품의 견적서를 받는다
# 푸붐의 존재여부에 따라서 yes or no 



# Solution
# 부품이 존재하면 yes 아니면 no를 리턴하는 함수



def binary_search(arr, target):
    
  start, end = 0, len(arr)-1
  
  while start <= end:
    mid = (start+end)//2
    
    if arr[mid]==target : return 'yes'
    elif arr[mid]<target : start=mid+1
    else: end= mid-1
  
  return 'no'    
  
  

def get_result(elements, targets):      
  elements.sort()    
  return list(map(lambda x: binary_search(elements, x), targets))



print(get_result([8,3,7,9,2],[5,7,9])  )
  
  
  

