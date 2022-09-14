from typing import List

class Solution:    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        width  = len(board[0])
        
        def accepted(opt,x,y) -> bool:
            
            # check column 
            for i in range(height):
                if board[i][x] == opt:
                    return False
                
            # check row
            for i in range(width):
                if board[y][i] == opt:
                    return False
            
            # check box
            xr = x % 3 # real x
            yr = y % 3 # real y
            for i in range(y-yr,y+abs(yr-3)):
                for j in range(x-xr,x+abs(xr-3)):
                    if board[i][j] == opt:
                        return False
            
            return True
            
        
        def backtracking(x,y) -> None:
            if x == width:
                y+= 1
                x = 0
            
            if x == 0 and y == height:
                return True
            else:             
                if board[y][x] == '.':
                    for opt in range(1,10):
                        if accepted(str(opt),x,y):
                            board[y][x] = str(opt)
                            if backtracking(x+1,y): return True
                            board[y][x] = '.'
                else:
                    if backtracking(x+1,y): return True
                    
                return False
        
        backtracking(0,0)


sudoku_map = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]

Solution().solveSudoku(sudoku_map) 
for row in sudoku_map:
    print(row)
        
        