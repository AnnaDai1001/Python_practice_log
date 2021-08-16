class Solution:
  def threeSum(self, nums, target):
    '''
      Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
      0 <= a, b, c, d < n
      a, b, c, and d are distinct.
      nums[a] + nums[b] + nums[c] + nums[d] == target
      You may return the answer in any order.
    '''
    # convert to a two sum questions with target as target - nums[i]
    nums.sort()
    output = []
    self.helper(nums, target, 4, [], output)
    return output
  
  def twoSum(self, nums, target):
    res = []
    start, end = 0, len(nums)-1
    while start < end:
      s = nums[start] + nums[end]
      if s == target:
        res.append([nums[start], nums[end]])
        start += 1
        end -= 1
        while start < end and nums[start-1] == nums[start]: start += 1
        while start < end and nums[end+1] == nums[end]: end -= 1
      elif s < target:
        start += 1
      else:
        end -= 1
    return res
  
  def helper(self, nums, target, K, res, output):
    if K > len(nums) or K < 2:
      return 
    if K == 2:
      output_2sum = self.twoSum(nums, target)
      for idx in output_2sum:
        output.append(res+idx)
    else:
      for i in range(len(nums)-K+1):
        if K*nums[i] > target or K*nums[-1] < target:
          break
        self.helper(nums[i+1:], target - nums[i], res + [nums[i]], output)
        



