class Solution:
  def Reverse_Integer(self, x):
    rev = int(str(abs(x))[::-1]) if x >= 0 else -int(str(abs(x))[::-1])
    return rev if rev.bit_length < 32 else 0 # or (rev >= -2**31 and rev <= 2**31-1)
                                                                
