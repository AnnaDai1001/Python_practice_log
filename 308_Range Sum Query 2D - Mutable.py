class NumMatrix(object):
    """
    Your NumMatrix object will be instantiated and called as such:
    obj = NumMatrix(matrix)
    obj.update(row,col,val)
    param_2 = obj.sumRegion(row1,col1,row2,col2)

    https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/75872/Python-94.5-Simple-sum-array-on-one-dimension-O(n)-for-both-update-and-sum

    beats 83.86%
    """
    # 用前缀和方法可以更高效，降低时间复杂度 O(n) 矩阵可变
    # Binary Index Tree ? 二进制个数加和
    
    def __init__(self, matrix):
      # each element of self.matrix is the sum of all the elements before it in this row
      r = len(matrix)
      c = len(matrix[0])
      for i in range(len(r)):
        for j in range(1,len(c)):
          matrix[i][j] += matrix[i][j-1]
      self.matrix = matrix
      
      def update(self, row, col, val):
        original = self.matrix[row][col]
        if col != 0:
          original -= self.matrix[row][col-1]
        diff = val - original
        for j in range(col, len(self.matrix[0])):
          self.matrix[row][j] += diff
      
      def sumRegion(self, row1, col1, row2, col2):
        # 一行一行的加， 区别对待第一列
        region_sum = 0
        for i in range(row1, row2+1):
          region_sum += self.matrix[i][col2]
          if col1 != 0:
            region_sum -= self.matrix[i][col1-1]
        return region_sum
          
    
