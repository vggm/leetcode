class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not n:
            return

        nums1_copy = nums1[:m]

        i,j = 0,0
        for k in range(n+m):
            if j >= n or (i < m and nums1_copy[i] < nums2[j]):
                nums1[k] = nums1_copy[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1


sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol.merge(nums1,m,nums2,n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol.merge(nums1,m,nums2,n)
print(nums1)

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
sol.merge(nums1,m,nums2,n)
print(nums1)

nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1
sol.merge(nums1,m,nums2,n)
print(nums1)

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5
sol.merge(nums1,m,nums2,n)
print(nums1)

"""

5

6
"""
nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
m = 5
nums2 = [-1,-1,0,0,1,2]
n = 6
Solution().merge(nums1,m,nums2,n)
print(nums1)

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
sol.merge(nums1,m,nums2,n)
print(nums1)

nums1 = [0,0,3,0,0,0,0,0,0]
m = 3
nums2 = [-1,1,1,1,2,3]
n = 6
Solution().merge(nums1,m,nums2,n)
print(nums1)
