class Solution:
  def valid_palindrome(s):
     # brute force
      s = s.lower()
      new = ''
      for c in s:
        if c.isalnum():
          new += c
      return new == new[::-1]
    
    
    # two pointer
    l,r = 0, len(s)-1
    while l<r:
      while l<r and not s[l].isalnum():
        l += 1
      while l<r and not s[r].isalnum():
        r -= 1
      if s[l] == s[r]:
        l += 1
        r -= 1
      else:
        return False
    return True
