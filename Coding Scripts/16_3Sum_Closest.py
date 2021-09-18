class Solution:
  def threeSumClosest(self, nums, target):
    '''
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    '''
    nums.sort()
    res = 0
    min_diff = float('inf')
    
    for i in range(len(nums)-2):
      first = nums[i]
      start, end = i+1, len(nums)-1
      while start < end:
        s = first + nums[start] + nums[end]
        diff = s - target
        if abs(diff) < min_diff:
          min_diff = abs(diff)
          res = s
          start += 1
          end -= 1
        elif diff < 0:
          start += 1
        else:
          end -= 1
     return res
      





