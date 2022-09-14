class Solution(object):
    def twoSum(self, nums: list, target: int) -> list:
        
        mem = {}
        
        for i, num in enumerate(nums):
            complementIndex = target - num
            
            if complementIndex in mem.keys():
                return [i, mem[complementIndex]]
            
            mem[num] = i
        
        
nums = [3,2,4]
target = 6

print(Solution.twoSum(Solution, nums, target))