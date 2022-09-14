from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        aCounter, bCounter = Counter(ransomNote), Counter(magazine)
        for letter in ransomNote:
            if bCounter[letter] < aCounter[letter]:
                return False

        return True


print(Solution().canConstruct("a","a"))