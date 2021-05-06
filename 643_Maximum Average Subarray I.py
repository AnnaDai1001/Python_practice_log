class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        i = 1
        stop = len(nums) - k
        temp_sum = sum(nums[:k])
        max_sum = temp_sum
        while i <= stop:
            temp_sum = temp_sum - nums[i-1] + nums[i+k-1]
            if temp_sum > max_sum:
                max_sum = temp_sum
            i = i + 1
        return max_sum/k
            
                
            
