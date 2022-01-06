def sum_of_left_leaves(self, root: TreeNode) -> int:
  res = 0
  stack = [(root,False)]
  while stack:
    curr, is_left = stack.pop()
    if not curr:
      continue
    if not curr.left and not curr.right:
      if is_left:
        res += curr.val
    else:
      stack.append((curr.left, True))
      stack.append((curr.right, False))
   return res
 

def sum_of_left_leaves(self, root: TreeNode) -> int:
  def dfs(node, is_left):
    if not node:
      return 0
    if not node.left and not node.right and is_left:
      return node.val
    return dfs(node.left, True) + dfs(node.right, False)
  return dfs(root, False)
