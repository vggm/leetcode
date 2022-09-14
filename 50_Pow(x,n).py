class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def bestPow(b: float, e: int) -> float:
            if e == 0: return 1
            if e == 1: return b
            
            h = bestPow(b,e//2)
            return h*h if e%2 == 0 else b*h*h
            

        res = bestPow(x,abs(n))
        return res if n >= 0 else 1/res
            

xn = input()
xn = xn.split()
x, n = float(xn[0]), int(xn[1])
print(Solution().myPow(x,n))