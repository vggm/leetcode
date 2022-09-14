from builtins import str


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeats = []
        s = s[::-1]
        
        max = 0
        cont = 0
        
        for c in s:
            if c not in repeats:
                cont += 1
                max = cont if max < cont else max
                repeats.append(c)
            else:
                cont = 1
                repeats = [c]
        
        return max


sol = Solution()
s = {"abcabcbb":3,"bbbbb":1,"pwwkew":3,"dvdf":3,"aab":2,"tmmzuxt":5,"abcb":3,"jlygy":4}

for str in s.keys():
    print("For the string {} the result is: {} - Expected {}".format(str,sol.lengthOfLongestSubstring(str),s[str]))