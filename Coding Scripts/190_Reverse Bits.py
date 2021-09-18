class Solution:
    def reverseBits(self, n: int) -> int:
        # Pythonic way
        bit_str = '{0:032b}'.format(n) # padding the 0s in the left
        reverse = bit_str[::-1]
        return int(reverse, 2)
