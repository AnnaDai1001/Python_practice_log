class Solution(object):
  def ValidWordSquare(self, words):
    n = len(words)
    for i in xrange(n):
      m = len(words[i])
      for j in xrange(m):
        try:
          if words[i][j] != words[j][i]:
            return False
        except:
          return False
    return True
