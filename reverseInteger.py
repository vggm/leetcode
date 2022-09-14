class Solution:
    def reverse(self, x: int) -> int:
        MAX_NUM = 2**31 - 1
        MIN_NUM = -2**31
        
        negative = False
        if x < 0:
            negative = True
            x *= -1
        
        x = int(str(x)[::-1])
        
        if not negative:
            return x if x < MAX_NUM else 0
        else:
            x *= -1
            return x if x > MIN_NUM else 0
        