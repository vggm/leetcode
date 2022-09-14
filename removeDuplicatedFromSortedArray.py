class Solution:
    """
    SIMPLE VERSION
    
    nums[:] = sorted(list(set(nums)))
    return len(nums)
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        
        k, prev = 0, None
        for n in nums:
            if n != prev:
                prev = n
                nums[k] = n
                k += 1
        
        return k
    
    
                
"""
[1,1,2]
[1,2,2]

[0,0,1,1,1,2,2,3,3,4]
[0,1,2,3,4,2,2,3,3,4]
"""

nums = [1,1,2]
Solution().removeDuplicates(nums)
print(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(nums)
print(nums)