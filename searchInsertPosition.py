class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        
        m = len(nums) // 2
        
        if m == 0:
            return 1 if target > nums[0] else 0
        
        if nums[m] == target:
            return m
        
        # search the middle right
        if nums[m] < target:
            return self.searchInsert(nums[m:],target) + len(nums)//2
        
        # search the middle left
        return self.searchInsert(nums[:m],target)
    
    
    ### ANOTHER SOLUTION ###
    def searchInsert2(self, nums: list[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (r-l+1)//2
            
            if nums[m] == m:
                return m
            
            if nums[m] < target:
                l = m+1
            else:
                r = m-1

        return l


nums = [1,2,4,5]
print(Solution().searchInsert2(nums,0))