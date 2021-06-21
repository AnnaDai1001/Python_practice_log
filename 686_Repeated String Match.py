class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 重点在于当a重复道足够长的时候，b还不在a里面则不存在
        
        l_a, l_b  = len(a), len(b)
        times = l_b//l_a + 2
        if b not in a*times:
            return -1
        while b in a*(times - 1):
            times -= 1
        return times
