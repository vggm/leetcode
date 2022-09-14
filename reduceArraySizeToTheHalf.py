from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        cnt = Counter(arr)      # Use Counter() to get numbers and their frequency
        num_freq = sorted(cnt.values(), reverse=True)  # Sort dictionary by their frequency (descending order)
        
        half_size = len(arr) // 2
        ans = 0
        
        while half_size > 0:
            half_size -= num_freq[ans]
            ans += 1
        
        return ans
        
arr = [3,3,3,3,5,5,5,2,2,7]
print(Solution.minSetSize(Solution,arr))

arr = [7,7,7,7,7,7]
print(Solution.minSetSize(Solution,arr))
        
arr = [1,9]        
print(Solution.minSetSize(Solution,arr))

arr = [1,2,3,4,5,6,7,8,9,10]
print(Solution.minSetSize(Solution,arr))
        
arr = [2,28,92,30,100,52,28,48,91,27,66,19,11,53,91,95,74,51,65,65,96,81,21,55,98,3,2,89,99,57,78,34,50,2,57,76,23,90,89,36,53,22,73,59,95,45]
print(Solution.minSetSize(Solution,arr))
