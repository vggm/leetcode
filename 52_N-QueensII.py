from copy import deepcopy


class Solution:
    def totalNQueens(self, n: int) -> int:
        arr = [-1 for _ in range(n)]
        global cnt
        cnt = 0
        def accepted(e):
            for i in range(e):
                if arr[i] == arr[e]: return False
                if abs(arr[i]-arr[e]) == abs(i-e): return False
            return True
              
        
        def backtracking(e):
            global cnt
            if e == n:
                cnt += 1
            else:
                for i in range(n):
                    arr[e] = i
                    if accepted(e):
                        backtracking(e+1)
        
        backtracking(0)
        return cnt