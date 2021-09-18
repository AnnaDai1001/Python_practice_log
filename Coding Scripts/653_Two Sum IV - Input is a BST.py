# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return False
        return self.helper(root, set(), k)
        
    def helper(self, node, nodes, k):
        if not node:
            return False
        c = k - node.val
        if c in nodes:
            return True
        nodes.add(node.val)
        return self.helper(node.left, nodes, k) or self.helper(node.right, nodes, k)
        # stack = [root]
        # val_list = []
        # while len(stack):
        #     curr = stack.pop()
        #     if curr:
        #         val_list.append(curr.val)
        #         stack.append(curr.left)
        #         stack.append(curr.right)
        # if len(val_list) > 1:
        #     for i in range(len(val_list)-1):
        #         for j in range((i+1),len(val_list)):
        #             if val_list[i] + val_list[j] == k:
        #                 return True
        # return False
