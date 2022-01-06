class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(strs):
            dic = {'1':1,
                  '2': 2,
                  '3': 3,
                   '4': 4,
                   '5': 5,
                   '6': 6,
                   '7': 7,
                   '8': 8,
                   '9': 9,
                   '0': 0               
                  }
            res = 0
            for s in strs:
                res = res * 10 + dic[s]
            return res
        return str(str2int(num1)+str2int(num2))
        
        # return str(int(num1)+int(num2))
