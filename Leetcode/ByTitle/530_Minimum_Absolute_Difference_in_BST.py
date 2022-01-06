# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
# Method 2 - recursion        
        # hard for me to understand
        
        
# Method 1:        
#         if not root:
#             return None
        
#         def traverse(node, res):
#             if not node: return None
#             traverse(node.left, res)
#             res.append(node.val)
#             traverse(node.right, res)
        
#         res = []
#         traverse(root,res)
#         diff_so_far = 9999
        
#         for i in range(0, len(res)-1):
#             if abs(res[i+1] - res[i]) < diff_so_far:
#                 diff_so_far = abs(res[i+1] - res[i])
        
#         return diff_so_far
          
