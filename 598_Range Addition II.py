class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # if not ops: return m*n
        # else:
        #     min_r = m
        #     min_c = n
        #     for op in ops:
        #         min_r = min(op[0], min_r)
        #         min_c = min(op[1], min_c)
        #     return min_r * min_c
        
        return min([op[0] for op in ops]) * min([op[1] for op in ops]) if ops else m * n
