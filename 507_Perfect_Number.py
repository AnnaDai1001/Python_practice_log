class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        perfect = False
        divisors = set([1])
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                divisors.add(num//i)
                divisors.add(i)
        if num != 1 and sum(divisors) == num:
            perfect = True
        return perfect
