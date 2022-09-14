from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtracking(n: int, e = 0, total = 0, sol = []):
            for i in range(e,n):
                total += candidates[i]
                
                if total <= target:
                    sol.append(candidates[i])
                    
                    if total == target:
                        res.append(list(sol))
                    else:
                        backtracking(n, i, total, sol)
                    
                    sol.pop()
                
                total -= candidates[i]
        
        backtracking(len(candidates))
        return res