class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0 
        res = []
        
        while i < len(nums):
            curr = nums[i]
            while i < (len(nums)-1) and nums[i+1]-nums[i]==1:
                i += 1
            if curr == nums[i]:
                res.append(str(nums[i]))
            else:
                res.append((str(curr) + "->" + str(nums[i])))
            i += 1
        return res
