class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        # 计数dic 然后按照key排序；算出相邻key差距为1是两个val的求和
        
        max_len = 0
        dic = Counter(nums)
        for key in dic:
            if key+1 in dic:
                max_len = max(max_len, dic[key+1] + dic[key])
        return max_len
