class Solution:
  def permutationInString(self, s1, s2):

    k = len(s1)
    for i in range(len(s2) - k + 1):
      temp = self.checkAnagram(s1, s2[i:i+k])
      if temp is True:
        return True
    return False
  
  def checkAnagram(self, s, t):
    s_list = sorted(s)
    t_list = sorted(t)
    return ''.join(s_list) == ''.join(t_list)
  
                               
