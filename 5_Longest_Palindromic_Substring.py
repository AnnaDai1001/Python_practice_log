class Solution:
  def longest_palindromic_substring(self, s):
    output = s[0] if s else ''
    dp = [[False]*len(s) for _ in range(len(s))]
    
    for i in range(len(s)):
      dp[i][i] = True
    
    for i in range(len(s)-1, -1, -1): #start from bottom right
      for j in range(i+1, len(s)):
        if s[i] == s[j]:
          if j-i == 1 or dp[i+1][j-1] is True:
            dp[i][j] = True
            if len(output) < len(s[i:j+1]):
              output = s[i:j+1]
     return output
                                 
          
          




