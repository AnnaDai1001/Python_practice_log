class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_pad = [0] + flowerbed + [0]
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed_pad[i:(i+3)] == [0,0,0]:
                flowerbed_pad[i+1] = 1
                count += 1
        
        return count >= n
