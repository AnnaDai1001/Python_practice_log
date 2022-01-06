class Solution:
    def checkRecord(self, s: str) -> bool:
        # return (s.count('A') < 2) & ('LLL' not in s)
        A, L = 0, 0
        for l in s:
            if l == 'A': A+=1
            elif l == 'L': L+=1
            if l != 'L': L=0
            if A > 1 or L > 2:
                return False
        return True
