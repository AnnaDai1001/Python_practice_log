# can use the solution of 4Sum but try a different one

class Solution:
  def threeSum(nums):
    '''
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
    '''
    nums.sort()
    added = set()
    output = []
    
    for i in range(len(nums)-2):
      first = nums[i]
      start, end = i+1, len(nums)-1
      while start < end:
        s = first + nums[start] + nums[end]
        if s == 0:
          if (first, nums[start], nums[end]) not in added:
            output.append([first, nums[start], nums[end]])
            added.add((first, nums[start], nums[end]))
          start += 1
          end -= 1
        elif s < 0:
          start += 1
        else:
          end -= 1
   return output
      
      
    
    
    
    
    
    

