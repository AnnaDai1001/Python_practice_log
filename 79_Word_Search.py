class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ### Solution 2 - same logic as solution 1 but reduce the number of cells to search so save much more time
        ROW, COL = len(board), len(board[0])
        
        def dfs(r,c,i):
            if len(word)==i:
                return True
            else:
                if 0<=r<ROW and 0<=c<COL and board[r][c]==word[i]:
                    board[r][c], tmp = '', board[r][c]
                    for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
                        if dfs(r+dx, c+dy, i+1):
                            return True
                    board[r][c] = tmp
            return False
        
        counter, searchset = Counter(word), []
        for r in range(ROW):
            for c in range(COL):
                counter[board[r][c]] -= 1
                if board[r][c]==word[0]:
                    searchset.append((r,c))
        if max(counter.values()) > 0: return False
        for r,c in searchset:
            if dfs(r,c,0):
                return True
        return False
        
        
        ### Solution 1 -  easier to understand
        # ROW, COL = len(board), len(board[0])
#         path = set() # make sure we didn't revisit
        
#         def dfs(r,c,i):
#             if i==len(word):
#                 return True
#             if ( r<0 or c<0 or
#                 r>=ROW or c>=COL or
#                 board[r][c] != word[i] or
#                 (r,c) in path
#             ):
#                 return False
#             path.add((r,c))
#             res = (dfs(r+1,c,i+1) or
#                   dfs(r-1,c,i+1) or
#                    dfs(r,c+1,i+1) or
#                    dfs(r,c-1,i+1)
#                   )
#             path.remove((r,c))
#             return res
        
        
        
#         for r in range(ROW):
#             for c in range(COL):
#                 if dfs(r,c,0): return True
#         return False
    
# # time complexity: O(m*n*4^word_len)

        
