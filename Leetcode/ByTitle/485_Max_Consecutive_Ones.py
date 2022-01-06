class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = count = 0
        for i in range(len(nums)):
            if nums[i]:
                count+=1
            else:
                maxcount=max(maxcount,count)
                count = 0
        
        return max(maxcount, count)
      
      
# one-line solution

#       return max(list(map(len, ("".join(list(map(str, nums)))).split('0'))))
