class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        nums = [i-64 for i in range(ord('A'), ord('Z')+1)]
        caps = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        dic = dict(zip(caps, nums))
        
        column_r = columnTitle[::-1]
        res = 0
        for i in range(len(column_r)):
            res += dic[column_r[i]] * (26**i)
        
        return res
