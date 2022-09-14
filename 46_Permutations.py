from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(n: int,possible: List[bool],sol: List[int]):
            if len(sol) == n:
                res.append(list(sol))
            else:
                for i in range(n):
                    if possible[i]:
                        possible[i] = False
                        sol.append(nums[i])
                        backtracking(n, possible, sol)
                        sol.pop()
                        possible[i] = True
        
        possible = [True for _ in range(len(nums))]
        sol = []
        backtracking(len(nums),possible,sol)
        
        return res