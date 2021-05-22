class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i += 1
                    j -= 1
                    # continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True
        
        # s_list = [i.lower() for i in s if i.isalnum()]
        # return s_list == s_list[::-1]
