class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # Boyer Moore Algorithm
        # cnt, element = 0, 0
        # for e in nums:
        #     if e == element:
        #         cnt += 1
        #     elif cnt == 0:
        #         cnt, element = 1, e
        #     else:
        #         cnt -= 1
        # return element 
        
        
        # Use hashtable
        n = len(nums)
        k = n//2
        counter = collections.Counter(nums)
        for i in set(nums):
            if counter.get(i) > k:
                return i
        
