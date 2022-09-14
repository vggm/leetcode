from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    check = board[i][j]
                    
                    # check column
                    for k in range(9):
                        if board[i][k] == check and k!=j:
                            return False
                        
                    # check row
                    for k in range(9):
                        if board[k][j] == check and k!=i:
                            return False
                    
                    #check box
                    xr = j%3
                    yr = i%3
                    for k in range(i-yr,i+abs(yr-3)):
                        for l in range(j-xr,j+abs(xr-3)):
                            if board[k][l] == check and (k!=i and l!=j):
                                return False
                    
        return True
                    