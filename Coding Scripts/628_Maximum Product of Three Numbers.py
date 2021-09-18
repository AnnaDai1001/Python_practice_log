class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # n time complexity
        smallestTwo = [float('inf')] * 2
        biggestThree = [float('-inf')] * 3
        for num in nums:
            if num < smallestTwo[0]:
                smallestTwo[0] = num
                smallestTwo.sort(reverse = True) # desc always (big, small) 小于大的
            if num > biggestThree[0]:
                biggestThree[0] = num
                biggestThree.sort() # asc 
                # 大于小的
        
        return max(biggestThree[0] * biggestThree[1] * biggestThree[2],
                  biggestThree[2] * smallestTwo[0] * smallestTwo[1])
        
        
        # nums = sorted(nums) # nlog(n) time complexity
        # nums.sort()
        # return max(nums[-1]*nums[-2]*nums[-3],
        #           nums[0]*nums[1]*nums[-1])
        
