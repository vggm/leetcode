class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        totalSize = len(nums1) + len(nums2)
        
        totalList = nums1 + nums2
        
        sort_list = sorted(totalList)
        
        if totalSize % 2 == 1:
            return sort_list[totalSize//2]
        else:
            return (sort_list[totalSize//2] + sort_list[totalSize//2-1]) / 2

nums1 = [1,3]
nums2 = [2]
print(Solution.findMedianSortedArrays(Solution,nums1,nums2))

nums1 = [1,2]
nums2 = [3,4]
print(Solution.findMedianSortedArrays(Solution,nums1,nums2))