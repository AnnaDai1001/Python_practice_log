# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
#         # recursion
#         res = []
#         self.dfs(root, res)
#         return res
    
#     def dfs(self, root, res):
#         if root:
#             self.dfs(root.left, res)
#             self.dfs(root.right, res)
#             res.append(root.val)
        
        # iteration
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                res.append(node.val)
        return res[::-1]
