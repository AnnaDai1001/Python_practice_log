class Solution:
    def isPalindrome(self, s: str) -> bool:
        # new = ''
        # s = s.lower()
        # for i in s:
        #     if i.isalnum():
        #         new += i
        # return new == new[::-1]
        
        # two pointer method
        s=s.lower()
        if len(s)<2: return True
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1    
            if s[left].isalnum() and s[right].isalnum():
                if s[left]==s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
        return True
