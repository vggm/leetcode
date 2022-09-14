class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        res = []

        for i in range(1,10):
            s = ""
            for j in range(n):
                if j == 0:
                    s += str(i)
                else:
                    if int(s[-1]) + k < 10:
                        s += str(i+k)
              
            if len(s) == n:          
                res.append(int(s))
                
        for i in range(1,10):
            s = ""
            for j in range(n):
                if j == 0:
                    s += str(i)
                else:
                    if int(s[-1]) - k >= 10:
                        s += str(i-k)
              
            if len(s) == n:          
                res.append(int(s))
                    
        return res
    
print(Solution().numsSameConsecDiff(3,7))