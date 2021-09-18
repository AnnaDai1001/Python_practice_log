
class MovingAverage():
  
  def __init__(self, size):
    self._size = size
    self._array = []
    self._sum = 0
   
  def next(self, val):
    self._sum += val
    self._array.append(val)
    if len(self._array) > self._size:
      self._sum -= self._array.pop(0)
    return self._sum/len(self._array)
  
 
# Time complexity: O(1); Space complexity: O(size)

# the class will be called as below
obj = MovingAverage(size)
param1 = obj.next(newval)
