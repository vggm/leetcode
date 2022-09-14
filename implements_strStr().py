class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if needle not in haystack: return -1
    
        nl = len(needle)
        for i in range(len(haystack)):
            if haystack[i:nl+i] == needle:
                return i
        
        return -1