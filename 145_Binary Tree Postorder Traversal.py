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
        
        # # iteration
        # ## 1.
        # res, stack = [], [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         res.append(node.val)
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return res[::-1]
    
        ## 2.
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res
