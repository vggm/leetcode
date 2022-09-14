class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        parcial,sol = "",""
        first_word = strs[0]
        
        i = 0
        while 1:
            try:
                parcial += first_word[i]
            except:
                break
            
            cnt = 0
            for str in strs[1:]:
                if parcial != str[:i+1]:
                    break
                cnt += 1
            
            if cnt != len(strs)-1:
                break
            
            sol = parcial
            
            i += 1 
        
        return sol
    


strs = ["flower","flow","flight"]
expected = "fl"
print("Solution {} - Expected {}".format(Solution.longestCommonPrefix(Solution,strs),expected))


strs = ["dog","racecar","car"]
expected = ""
print("Solution {} - Expected {}".format(Solution.longestCommonPrefix(Solution,strs),expected))
