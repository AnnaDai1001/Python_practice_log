"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Recursive 迭代，调用自身
        def rec(node):
            if node:
                out.append(node.val)
                for i in node.children:
                    rec(i)
        
        out = []
        rec(root)
        return out
        # Iterative 按顺序访问线性结构的每一项
        # if not root: return []
        # stack = [root]
        # res = []
        # while len(stack):
        #     temp = stack.pop()
        #     res.append(temp.val)
        #     stack.extend(reversed(temp.children))
        # return res
