'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.
For example, Given s = “eceba” and k = 2,
T is "ece" which its length is 3.
'''


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # https://www.cnblogs.com/lz87/p/10095363.html
        # https://github.com/scottliu77/leetcode/blob/master/python-leetcode/340-longest-substring-with-at-most-k-distinct-characters.py
        # sliding window keep track of checked substrings
        start = 0
        res = 0
        d = {} # sliding window tracker, need to keep length smaller than or equal to k
        for i in xrange(len(s)):
          d[s[i]] = i
          if len(d) > k:
            start = min(d.values())
            del d[s[start]]
            start += 1
          res = max(res, i - start + 1)
        return res
        
        
#         # Brute Force: find all the substrings and find the max length of substrings that contains k distinct chars - O(n^3)
#         res = 0
#         for i in xrange(len(s)):
#           for j in xrange((i+1), len(s)):
#             curr = s[i:j]
#             d = collections.Counter(curr)
#             if len(d.keys()) <= k:
#               res = max(res, len(curr))
#         return res
              
        
