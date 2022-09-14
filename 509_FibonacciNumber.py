class Solution:
    def fib(self, n: int) -> int:
        
        a = 0
        b = 1
        
        if n == 0: return a
        if n == 1: return b
        
        for i in range(2,n+1):
            a,b = b, b+a
        
        return b
    
    
    def fibList(self, n: int) -> int:
        memo = [0,1]
        
        for i in range(2,n+1):
            memo.append(memo[i-1]+memo[i-2])
            
        return memo[n]
    
    
    def fibDict(self, n: int, dict = {}) -> int:
        if n in dict: return dict[n]
        if n == 0: return 0
        if n == 1: return 1
        dict[n] = self.fibDict(n-1)+self.fibDict(n-2)
        return dict[n]
    
    
    def fibRecursive(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        return self.fibRecursive(n-1    )+self.fibRecursive(n-2)
        
    
for i in range(100):
    print(i, ": ", Solution().fib(i),sep="")