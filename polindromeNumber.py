class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
        for x,y in zip(str(x),str(x)[::-1]):
            if x != y:
                return False
            
        return True
    
x = 121
print("{} es un palindromo: {}".format(x,Solution.isPalindrome(Solution,x)))

x = -121
print("{} es un palindromo: {}".format(x,Solution.isPalindrome(Solution,x)))

x = 10
print("{} es un palindromo: {}".format(x,Solution.isPalindrome(Solution,x)))

x = 123
print("{} es un palindromo: {}".format(x,Solution.isPalindrome(Solution,x)))

x = 1
print("{} es un palindromo: {}".format(x,Solution.isPalindrome(Solution,x)))

x = -1
print("{} es un palindromo: {}".format(x,Solution.isPalindrome(Solution,x)))