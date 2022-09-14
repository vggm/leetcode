class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mem = {}
        
        for x in nums:
            if mem.get(x) != None:
                return True
            
            mem[x] = 1
            
        return False