class Solution(Object):
  def longestConsecutive(self, root):
    if not root:
      return 0
    self.res = 1
    
    def dfs(node, parent_val, temp_res):
      if not node:
        return 
      if node.val == parent_val + 1:
        temp_res += 1
        self.res = max(self.res, temp_res)
      else:
        temp_res = 1
      
      dfs(node.left, node.val, temp_res)
      dfs(node.right, node.val, temp_res)
      
    dfs(root.left, root.val, 1)
    dfs(root.right, root.val, 1)
    
    return self.res

