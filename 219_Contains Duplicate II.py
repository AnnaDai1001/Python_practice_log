class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
        
#         dic = {}
#         for i, v in enumerate(nums):
#             if v not in dic:
#                 dic[v] = i
#             else:
#                 idx_diff = i - dic[v]
#                 if idx_diff <= k:
#                     return True
#                 else:
#                     dic[v] = i
#         return False
