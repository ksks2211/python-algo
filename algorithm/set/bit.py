class BitSet:
  def __init__(self, MAX=31) -> None:
    self.S = 0
    self.MAX=MAX
  
  def clear(self) ->None:
    self.S=0
  
  def add(self, el:int)->None:
    self.S = self.S | (1 << el)
  
  def remove(self, el:int)->None:
    self.S = self.S &~(1<<el)    
  
  def toggle(self, el:int)->None:
    self.S = self.S ^ (1<<el)
  
  def has(self, el:int)->None:
    return 0 != (self.S & (1<<el))
  
  def __iter__(self):    
    for i in range(0, self.MAX+1):
      if self.has(i): yield i
    
  