class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        caps = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        res = []
        while columnNumber != 0:
            temp = (columnNumber-1)%26
            res.append(caps[temp])
            columnNumber = (columnNumber-1)//26
        return ''.join(res[::-1])
        
        
#         caps = [chr(i) for i in range(ord('A')-1, ord('Z')+1)]
#         res = []
        
#         while columnNumber != 0:
#             temp = columnNumber%26
#             if temp == 0:
#                 res.append(caps[26])
#                 columnNumber = (columnNumber-26)//26
#             else:
#                 res.append(caps[temp])
#                 columnNumber = (columnNumber-temp)//26
        
#         return ''.join(res[::-1])
        
        
