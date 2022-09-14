class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = s.split(' ')
        last = -9999
        
        digit = "1234567890"
        
        for x in arr:
            if x.isdecimal():
                if int(x) > last:
                    last = int(x)
                else:
                    return False
        
        return True
    
    
s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
expected = True
print("solution {} - expected {}".format(Solution.areNumbersAscending(Solution,s), expected))

s = "hello world 5 x 5"
expected = False
print("solution {} - expected {}".format(Solution.areNumbersAscending(Solution,s), expected))

s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
expected = False
print("solution {} - expected {}".format(Solution.areNumbersAscending(Solution,s), expected))
