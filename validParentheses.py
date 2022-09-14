class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')':'(',
                ']':'[',
                '}':'{'}
        
        stack = []
        
        for c in s:
            if c not in dict:
                stack.append(c)
            else:
                if not stack or dict[c] != stack.pop():
                    return False
        
        return not stack
    

sol = Solution()
s = "]"
expected = False
print("solution {} - expected {}".format(sol.isValid(s),expected))