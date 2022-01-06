"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # iteration
        if not root: return []
        stack = [root]
        res = []
        while len(stack):
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children or [])
        return res[::-1]
        
        # recursion
        # def rec(node):
        #     if node:
        #         for child in node.children:   
        #             rec(child)
        #         res.append(node.val)
        # res = []        
        # rec(root)
        # return res
