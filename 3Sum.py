from typing import Counter


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i

        stack = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if hashMap.get(-(nums[i]+nums[j])):
                    k = hashMap[-(nums[i]+nums[j])]
                    if i != k and j != k:
                        stack.append([nums[i],nums[j],nums[k]])

        return stack


print(Solution().threeSum([-1,1,0,2,-1,-4]))