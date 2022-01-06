class Solution:
  def findAllAnagramsinString(self, s, p):
    # method 1 - sliding window:
    anagram = ''.join(sorted(p))
    window_string = ''
    window_start = 0
    start_indices = []
    for c in s:
      window_string += c
      if len(window_string) == len(anagram):
        if ''.join(sorted(window_string)) == anagram:
          start_indices.append(window_start)
        window_string = window_string[1:]
        window_start += 1
   return start_indices

  # fastest approach - hash values
  k = len(p)
  output = []
  hashofp = sum(hash(x) for x in p)
  currenthash = sum(hash(x) for x in s[:k])
  if hashofp == currenthash:
    output.append(0)
  
  for i, l in enumerate(s[k:]):
    currenthash += hash(l) - hash(s[i])
    if hashofp == currenthash:
      output.append(i+1)
  return output
  
    
    
    
    
