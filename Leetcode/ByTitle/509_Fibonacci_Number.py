class Solution:
    def fib(self, n: int) -> int:
        # if n==0 or n==1: return n
        # if n>1: return self.fib(n-1)+self.fib(n-2)
        
        # memorized method
        memo = [0,1]
        for i in range(2,n+1):
            memo.append(memo[i-1]+memo[i-2])
        return memo[n]
