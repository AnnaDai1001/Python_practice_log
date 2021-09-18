# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res = []
        def rec(node):
            if not node:
                return 
            
            res.append(str(node.val))
            
            if not node.left and not node.right:
                return 
            
            res.append('(')
            rec(node.left)
            res.append(')')
            
            if node.right:
                res.append('(')
                rec(node.right)
                res.append(')')
            
        rec(t)
        return ''.join(res)
                
