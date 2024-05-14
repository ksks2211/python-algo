from collections import Counter





def count_element(elements, element):
  counter = Counter(elements)  
  return counter[element]



def unique_elements(elements):
  counter = Counter(elements)  
  return counter.keys()