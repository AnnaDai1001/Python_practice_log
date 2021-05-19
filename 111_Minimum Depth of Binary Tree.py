# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # DFS
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # elif not root.left:
        #     return self.minDepth(root.right) + 1
        # elif not root.right:
        #     return self.minDepth(root.left) + 1
        # else:
        #     return min(map(self.minDepth, (root.left, root.right))) + 1
        
        # BFS
        queue = [(root, 1)]
        
        while queue:
            next_visit, curr_len = queue.pop(0)
            if not next_visit:
                continue
            if not next_visit.left and not next_visit.right:
                return curr_len
            
            queue.append((next_visit.left, curr_len+1))
            queue.append((next_visit.right, curr_len+1))
        
        return 0
