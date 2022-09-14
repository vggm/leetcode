from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = True
        i = len(digits)-1
        while i >= 0 and carry:
            
            if digits[i] == 9:
                digits[i] = 0
            
            else:
                digits[i] += 1
                carry = False
            
            i -= 1
        
        if carry:
            # insert 1 in the position 0
            digits.insert(0,1)
        
        return digits


print(Solution().plusOne([9]))