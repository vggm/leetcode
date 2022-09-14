class Solution:
    def checkString(self, s: str) -> bool:
        canBeA = True
        
        for x in s:
            if not canBeA and x == 'a':
                return False
            
            if canBeA and x == 'b':
                canBeA = False    
            
        return True
    
    
sol = Solution()

s = "aaabbb"
expected = True
print("solution {} - expected {}".format(sol.checkString(s), expected))

s = "ababab"
expected = False
print("solution {} - expected {}".format(sol.checkString(s), expected))

s = "bbb"
expected = True
print("solution {} - expected {}".format(sol.checkString(s), expected))

s = "aaaabbb"
expected = True
print("solution {} - expected {}".format(sol.checkString(s), expected))

s = "aaaabbb"
expected = True
print("solution {} - expected {}".format(sol.checkString(s), expected))