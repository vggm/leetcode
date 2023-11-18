
class Solution:
  def threeSumClosest(self, nums: list[int], target: int) -> int:
    sorted_nums = sorted(nums)
    md = float('inf')
    ms = float('inf')
    
    for i, a in enumerate(sorted_nums):
      l = i+1
      r = len(sorted_nums)-1
      
      while l < r:
        b, c = sorted_nums[l], sorted_nums[r]
        
        t = a+b+c
        d = abs(t-target)
        if d == 0: return t
        if d < md:
          md = d
          ms = t
        
        if t > target:
          r -= 1
        else: # t < target
          l += 1
    
    return ms

solution = Solution()
res = solution.threeSumClosest( [0,0,0], 1 )
print(res)