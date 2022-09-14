class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0,1]
        
        i = 0
        while i < n:
            distinct_ways = memo[-1]+memo[-2]
            memo.append(distinct_ways)
            i+=1
        
        return distinct_ways
        
    
print(Solution().climbStairs(35))