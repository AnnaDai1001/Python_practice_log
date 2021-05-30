class Solution:
    def isHappy(self, n: int) -> bool:
        # Method 1:
        # memo = set()
        # while n != 1:
        #     n = sum(int(i)**2 for i in str(n))
        #     if n in memo:
        #         return False
        #     else:
        #         memo.add(n)
        # else:
        #     return True
        
        # Method 2:
        memo = set()
        while n not in memo:
            memo.add(n)
            n=sum(int(i)**2 for i in str(n))
        return 1 in memo # or n == 1
