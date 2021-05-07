class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # n*(n+1)//2 # the sum of 1 to n
        ex = sum(set(range(1,len(nums)+1))) - sum(set(nums))
        dup = sum(nums) - sum(set(nums))
        return [dup, ex]
