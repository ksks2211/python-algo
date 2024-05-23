


def get_result(input):
  
  
  result = []
  n = 0
  
  has_num = False
  
  for c in list(input):                
    if c.isdigit(): 
      has_num = True
      n+=int(c)
    else:
      result.append(c)
  
  result.sort()    
  
  if has_num : result.append(str(n))
  return "".join(result)


print(get_result("K1KA5CB7"))