class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1 or carry == 1:
                digit = digits[i] + 1
                if digit == 10:
                    res.append(0)
                    carry = 1
                else:
                    res.append(digit)
                    carry = 0
            else:
                res.append(digits[i])
        if carry == 1:
            res.append(1)
        return res[::-1]

        
#         val = 0
#         for digit in digits:
#             val = val*10 + digit
#         val_p1 = val + 1
#         digits_p1 = []
        
#         while val_p1 > 0:
#             digits_p1.append(val_p1%10)
#             val_p1 = val_p1//10
        
#         return digits_p1[::-1]
        
