# Solution 1: 到每一个位置都重新数一次上下左右
class Solution(object):
  def maxKilledEnermies(self, grid):
    def count(x,y):
      left, right, up, down = 0, 0, 0, 0
      for i in range(x-1, -1, -1):
        if grid[i][y]=='W':
          break
        if grid[i][y]=='E':
          up += 1
     
     for i in range(x+1, row):
        if grid[i][y]=='W':
          break
        if grid[i][y]=='E':
          down += 1
     
     for j in range(y-1, -1, -1):
        if grid[x][j]=='W':
          break
        if grid[x][j]=='E':
          left += 1
     
     for j in range(y+1, col):
        if grid[x][j]=='W':
          break
        if grid[x][j]=='E':
          right += 1
     return left+right+up+down
     
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    ans = 0
    for r in range(row):
      for c in range(col):
         ans = max(ans, count(r,c))
    return ans
 
# Time complexity: O(mn(m+n)); Space Complexity: O(1)


# Solution 2: 构建一个arr来存储每个位置的最大数目，最后一次遍历的时候更新ans; 每一行都初始化一个count，遇到E就加一，遇到W就归零，遇到0就可以赋值给arr
# Time complexity: O(4mn); Space complexity: O(mn)

class Solution(object):
  def maxKilledEnermies(self, grid):
    if not grid: return 0
    row, col = len(grid), len(grid[0])
    ans = 0
    arr = [[0]*col for r in range(row)]
    
    # from left to right
    for i in range(row):
      count = 0
      for j in range(0,col,1):
        if grid[i][j] == 'E':
          count += 1
        elif grid[i][j] == 'W':
          count = 0
        else:
          arr[i][j] += count
    # from right to left
    for i in range(row):
      count = 0
      for j in range(col-1, -1, -1):
        if grid[i][j] == 'E':
          count += 1
        elif grid[i][j] == 'W':
          count = 0
        else:
          arr[i][j] += count
     # from up to down
    for j in range(col):
      count = 0
      for i in range(0, row, 1):
        if grid[i][j] == 'E':
          count += 1
        elif grid[i][j] == 'W':
          count = 0
        else:
          arr[i][j] += count
          
    # from down to up
    for j in range(col):
      count = 0
      for i in range(row-1, -1, -1):
        if grid[i][j] == 'E':
          count += 1
        elif grid[i][j] == 'W':
          count = 0
        else:
          arr[i][j] += count
          ans = max(ans, arr[i][j])
    return ans
    
    
    
    
                     
                     
