# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

        
        # recursive
        
#         # 1
#         if not root:return []
#         res = []
#         res+=self.inorderTraversal(root.left)
#         res.append(root.val)
#         res+=self.inorderTraversal(root.right)
#         return res
        
#         # 2
#         def rec(node):
#             if node:
#                 rec(node.left)
#                 res.append(node.val)
#                 rec(node.right)
        
#         res = []
#         rec(root)
#         return res
