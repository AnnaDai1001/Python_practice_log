# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        # DFS method
        def helper(node: TreeNode) -> tuple:
            if not node:
                return 0, 0
            else:
                left_sum, left_tilt = helper(node.left)
                right_sum, right_tilt = helper(node.right)
                
                current_tilt = abs(left_sum - right_sum)
                return ((left_sum+node.val+right_sum), left_tilt+current_tilt+right_tilt)
        
        return helper(root)[1]
