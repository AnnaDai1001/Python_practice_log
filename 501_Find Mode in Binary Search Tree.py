# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        ans = []
        queue = deque([root])
        ans.append(root.val)
        while queue:
            node = queue.pop()
            
            if node.left:
                ans.append(node.left.val)
                queue.append(node.left)
                
            if node.right:
                ans.append(node.right.val)
                queue.append(node.right)
        c = max(Counter(ans).values())
        return[k for k,v in Counter(ans).most_common() if v==c]
       # return[k for k,v in list(Counter(ans).items()) if v==c]
