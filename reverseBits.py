class Solution:
    def reverseBits(self, n: int) -> int: 
        
        # bin(n) returns the binary representation of n but 0b...
        # to avoid 0b... we use [2:]
        
        # zfill(n) add zeros to complete n size of the number
        
        # int(n,2) returns the decimal representation of n (base 2)
             
        return int(str(bin(n)[2:].zfill(32))[::-1],2)
    
    
sol = Solution()
n = 0b00000010100101000001111010011100
expected = 964176192
print("solution {} - expected {}".format(sol.reverseBits(n),expected))