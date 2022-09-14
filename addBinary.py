def maxMin(a, b):
    if len(a) > len(b):
        return a[::-1], b[::-1]
    else:
        return b[::-1], a[::-1]
        
        
def xor(x, y) -> bool:
    return (x and not y) or (not x and y)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        
        greater, lower = maxMin(a, b)
        
        for i in range(len(greater) - len(lower)):
            lower += "0"
            
        result = ""
        for x, y in zip(greater, lower):
            x = True if x == "1" else False
            y = True if y == "1" else False
            
            toAdd = xor(x, y)
            
            if carry:
                aux = toAdd
                toAdd = xor(toAdd, carry)
                carry = (aux and carry) or (x and y)
            else:
                carry = x and y
            
            result += "1" if toAdd == True else "0"          
            
        if carry:
            result += "1"
            
        return result[::-1]
            
sol = Solution()
a = "11"
b = "1"
print(sol.addBinary(a,b))   

a = "1010"
b = "1011"
print(sol.addBinary(a,b))   

a = "0"
b = "0"
print(sol.addBinary(a,b))   

a = "1"
b = "0"
print(sol.addBinary(a,b))   

a = "1111"
b = "1111"
print(sol.addBinary(a,b))   
        
        
    
