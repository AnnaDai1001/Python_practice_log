class Solution:
  def valid_anagram(self, s1, s2):
    # hash table
    d1 = dict()
    d2 = dict()
    if len(s1) != len(s2):
      return False
    for i in range(len(s1)):
      if s1[i] in d1:
        d1[s[i]] += 1
      else:
        d1[s[i]] = 1
      if s2[i] in d2:
        d2[s[i]] += 1
      else:
        d2[s[i]] = 1
    return d1 == d2
  
  
  # Sorted
    s1_list = sorted(s1)
    s2_list = sorted(s2)
    return "".join(s1_list) == "".join(s2_list)
