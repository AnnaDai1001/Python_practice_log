# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # DFS
        
        # BFS -  usually use queue; isolate each row using pop and queue children
        q, res = [root], []
        while len(q):
            qlen, row_sum = len(q), 0
            for i in range(qlen):
                curr = q.pop(0)
                row_sum += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            res.append(row_sum/qlen)
        return res
        
        # BFS without queue
        res = []
        level = (root, )
        while len(level):
            res.append(sum(node.val for node in level)/len(level))
            level = tuple(child for node in level for child in (node.left, node.right) if child)
            
        return res
            
