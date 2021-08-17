
class Solution:
  def number_of_islands(self, grid):
    output = 0
    if not grid: return output
    m,n = len(grid), len(grid[0])
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1':
          output += 1
          self.dfs_helper(grid,i,j)
    return output
  
  def dfs_helper(self, grid, x, y):
    if x >= 0 and x < len(grid) and y >= 0  and y < len(grid[0]) and grid[x][y] == '1':
      grid[x][y] = '2'
      self.dfs_helper(grid, x-1, y)
      self.dfs_helper(grid, x+1, y)
      self.dfs_helper(grid, x, y-1)
      self.dfs_helper(grid, x, y+1)






