from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle = []
        
        for i in range(numRows):
            triangle.append([1] * (i+1))
            for j in range(1,i):
                triangle[i][j] = triangle[i-1][j-1]+triangle[i-1][j]
        
        return triangle

n = 8
for i,row in enumerate(Solution().generate(n)):
    print(" "*(n-i-1),row,sep="")
