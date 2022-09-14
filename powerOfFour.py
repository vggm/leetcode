class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        i = 0
        while 1:
            
            if 4**i == n:
                return True
            
            if 4**i > n:
                return False
            
            i += 1
    
    
sol = Solution()
n = 16
expected = True
print("solution {} - expected {}".format(sol.isPowerOfFour(n), expected))

n = 5
expected = False
print("solution {} - expected {}".format(sol.isPowerOfFour(n), expected))

n = 1
expected = True
print("solution {} - expected {}".format(sol.isPowerOfFour(n), expected))
