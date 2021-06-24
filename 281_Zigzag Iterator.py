class Zigzag:
  def __init__(self, v1, v2):
    self.arrs = [v1, v2]
    self.queue = deque()
    
    for i in range(0,2):
      if len(self.arrs[i]) > 0:
        self.queue.append((i,0))
        
  def next(self):
    if self.queue()
      arr_idx, elem_idx = self.queue.popleft()
      next_elem_idx = elem_idx + 1
      if next_elem_idx < len(self.arrs[arr_idx]):
        self.queue.append((arr_idx, next_elem_idx))
      return self.arrs[arr_idx][elem_idx]
    
    raise Exception
    
  def hasNext(self):
    return len(self.queue) > 0
      
    
