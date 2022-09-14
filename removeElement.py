class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        l,r,cnt = 0, len(nums)-1, 0
        while l <= r:
            if nums[l] == val and nums[r] != val:
                nums[l] = nums[r]
                l += 1
                r -= 1
                cnt += 1
            elif nums[l] == val and nums[r] == val:
                r -= 1
                cnt += 1
            else:
                l += 1
                
        return len(nums) - cnt
                
    
    
nums = [3,2,2,3]
Solution().removeElement(nums,3)
print(nums)
        
nums = [0,1,2,2,3,0,4,2]
Solution().removeElement(nums,2)
print(nums)

nums = [1]
print(Solution().removeElement(nums,1))