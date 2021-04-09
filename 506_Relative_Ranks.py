class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = sorted(score, reverse = True)
        result = {}
        
        for i in range(len(score)):
            if i == 0:
                result[arr[i]] = "Gold Medal"
            if i == 1:
                result[arr[i]] = "Silver Medal"
            if i == 2:
                result[arr[i]] = "Bronze Medal"
            if i > 2:
                result[arr[i]] = str(i+1)
        
        return list(map(lambda x: result[x], score))
