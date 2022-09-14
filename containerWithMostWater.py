class Solution:
    def maxArea(self, height: list[int]) -> int:

        currArea, res = 0,0

        l,r = 0,len(height)-1
        while l < r:
            currArea = (r-l) * min(height[l],height[r])
            res = max(res,currArea)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return res


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))
