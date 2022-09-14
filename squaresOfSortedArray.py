class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [x*x for x in nums]
        res.sort()
        return res




nums = [-4,-1,0,3,10]
print(Solution().sortedSquares(nums))