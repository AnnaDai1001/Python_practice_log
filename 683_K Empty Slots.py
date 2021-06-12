# Link: https://www.programmersought.com/article/69372392824/


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        
        days = [0]*len(flowers)
        # get reversed list: days of each flower blossoms
        for i in xrange(len(flowers)):
          days[flowers[i]-1] = i+1
        result = float('inf')
        i, left, right = 0, 0, k+1
        while right < len(days):
          if days[i] < days[left] or days[i] <= days[right]:
            if days[i] == days[right]:
              result = min(result, max(days[left], days[right]))
            left, right = i+1, i+2+k
          i += 1
        return -1 if result == float('inf') else result
        
