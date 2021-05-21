class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            # offset of previous rows - smart
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]
#         if numRows == 1:
#             return [[1]]
#         if numRows == 2:
#             return [[1], [1,1]]
        
#         res = [[1], [1,1]]
#         for l in range(2, numRows):
#             prev = res[(l-1)]
#             curr = [1]
#             for j in range((l-1)):
#                 curr.append((prev[j] + prev[j+1]))
#             curr.append(1)
#             res.append(curr)
#         return res
            
