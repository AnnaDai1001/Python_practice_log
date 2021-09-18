class Solution:
  def twoSum(nums, target):
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    Suppose there is only one answer
    '''
    # Brute Force
    n = len(nums)
    for i in range(n-1):
      for j in range(i+1, n):
        if nums[i] + nums[j] == target:
          return [i,j]
        
    # Use dict to reduce the computation time
    d = dict()
    n = len(nums)
    for i in range(n):
      comp = target - nums[i]
      if comp not in d:
        d[nums[i]] = i
      else:
        return [d[comp], i]
    
    # Use two pointer and generalize to at least one set of result
    
    nums.sort()
    res = [] # generalize to at least one pair
    start, end = 0, len(nums)-1
    while start < end:
      s = nums[start] + nums[end]
      if s == target:
        res.append([start, end])
        start += 1
        end -= 1
        # if we are going to output values and do not want duplicates
        # need to run the following and also change line 32 above to res.append([nums[start], nums[end]])
#         while start < end and nums[start-1] == nums[start]: start += 1
#         while start < end and nums[end+1] == nums[end]: end -= 1
      elif s < target:
        start += 1
      else:
        end -= 1
    return res




