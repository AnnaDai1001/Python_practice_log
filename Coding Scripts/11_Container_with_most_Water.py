class Solution:
  def container_max_water(self, height):
    '''
    trade off between height and width
    '''
    l, r = 0, len(height)
    area = 0
    while l < r:
      temp = min(height[l], height[r]) * (r-l)
      area = max(area, temp)
      if height[l] < height[r]:
        l += 1
      else:
        r += 1
     return area
  
  # or brute force
    








