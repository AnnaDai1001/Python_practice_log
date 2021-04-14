class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        if len(s) < k: return s[::-1]
        # if len(s) < 2*k: return s[:k][::-1]+s[k:]
        return s[:k][::-1]+s[k:2*k]+self.reverseStr(s[2*k:],k) 
        
#         l = len(s)
#         n = l//(2*k)
#         m = l%(2*k)
#         res = ''
#         for i in range(n):
#             res += s[(2*k*i):(2*k*i+k)][::-1]
#             res += s[(2*k*i+k):(2*k*i+2*k)]
#         if m > 0 and m < k:
#             res += s[(2*k*n):(2*k*n+m)][::-1]
#         else:
#             res += s[(2*k*n):(2*k*n+k)][::-1]
#             res += s[(2*k*n+k):(2*k*n+m)]
        
#         return res
    
    
