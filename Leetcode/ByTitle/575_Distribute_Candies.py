class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return len(set(candyType)) if len(candyType)//2 > len(set(candyType)) else len(candyType)//2
