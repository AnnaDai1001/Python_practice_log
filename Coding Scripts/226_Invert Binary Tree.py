# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Iterative method
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
        
        # # Another recurrsion
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.interTree(root.left)
        #     return root
       
    # Below is my own solution
#         if not root:
#             return root
        
#         res = TreeNode(root.val)
#         def dfs(node, newtree):
#             if node.left and node.right:
#                 newtree.left = TreeNode(node.right.val)
#                 newtree.right = TreeNode(node.left.val)
#                 dfs(node.right, newtree.left)
#                 dfs(node.left, newtree.right)
#             elif node.left:
#                 newtree.right = TreeNode(node.left.val)
#                 dfs(node.left, newtree.right)
#             elif node.right:
#                 newtree.left = TreeNode(node.right.val)
#                 dfs(node.right, newtree.left)
#         dfs(root, res)
        
#         return res
