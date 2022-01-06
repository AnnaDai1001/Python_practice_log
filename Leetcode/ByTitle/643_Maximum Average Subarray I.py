class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        store_sum = sum(nums[:k])
        max_sum = store_sum
        
        # M1
        for i in range(1,len(nums)-k+1):
            store_sum = store_sum - nums[i-1] + nums[i+k-1]
            if store_sum > max_sum:
                max_sum = store_sum
        
        # M2 - Time Limit Exceeded
        # for i in range(1, len(nums)-k+1):
        #     store_sum = sum(nums[i:(i+k)])
        #     if store_sum > max_sum:
        #         max_sum = store_sum
        
        # M3
        # i = 1
        # while i <= (len(nums) - k):
        #     store_sum = store_sum - nums[i-1] + nums[i+k-1]
        #     if store_sum > max_sum:
        #         max_sum = store_sum
        #     i += 1
                   
        return max_sum/k
            
