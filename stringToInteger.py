class Solution:
    def myAtoi(self, s: str) -> int:
        wo_spaces = s.strip()
    
        if len(wo_spaces) == 0:
            return 0

        negative, positive = False, False
        if wo_spaces[0] == '-':
            negative = True
        elif wo_spaces[0] in '+':
            positive = True
        elif wo_spaces[0] not in "1234567890":
            return 0
        
        MAX_NUM = 2**31 - 1
        MIN_NUM = -2**31
            
        number = 0
        i = 1 if negative or positive else 0
        while i < len(wo_spaces):
            if wo_spaces[i] in "1234567890":
                
                curr_digit = ord(wo_spaces[i]) - ord('0')
                
                number = number*10 + curr_digit
                
            else:
                break
            i += 1
            
        if not negative:
            return number if number < MAX_NUM else MAX_NUM
        else:
            return -number if -number > MIN_NUM else MIN_NUM
        
    
    
s = "42"
expected = 42
print("solution {} - expected {}".format(Solution.myAtoi(Solution,s), expected))

s = "           -42"
expected = -42
print("solution {} - expected {}".format(Solution.myAtoi(Solution,s), expected))

s = "480 with words"
expected = 480
print("solution {} - expected {}".format(Solution.myAtoi(Solution,s), expected))

s = "words and 987"
expected = 0
print("solution {} - expected {}".format(Solution.myAtoi(Solution,s), expected))

s = "3.14159"
expected = 3
print("solution {} - expected {}".format(Solution.myAtoi(Solution,s), expected))

s = ""
expected = 0
print("solution {} - expected {}".format(Solution.myAtoi(Solution,s), expected))

s = "+1"
expected = 1
print("solution {} - expected {}".format(Solution.myAtoi(Solution,s), expected))
