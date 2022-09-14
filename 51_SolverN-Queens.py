from copy import deepcopy
from typing import List


class Solution:
    
    def solToBoard(self,sol: list, n: int) -> List[str]:
        board = ['']*n
        for i in range(n):
            for j in range(n):
                board[i] += 'Q' if sol[i] == j else '.'
        return board
        
    
    def solveNQueens(self, n: int) -> list[list[str]]:
        arr = [-1 for _ in range(n)]
        solutions = []
        def accepted(e):
            for i in range(e):
                if arr[i] == arr[e]: return False
                if abs(arr[i]-arr[e]) == abs(i-e): return False
            return True
              
        
        def backtracking(e):
            if e == n:
                solutions.append(deepcopy(arr))
            else:
                for i in range(n):
                    arr[e] = i
                    if accepted(e):
                        backtracking(e+1)
        
        backtracking(0)
        
        boards = []
        for sol in solutions:
            boards.append(self.solToBoard(sol,n))
        return boards
    

for sol in Solution().solveNQueens(4):
    for row in sol:
        print(row)
    print("#"*len(row))
        
        