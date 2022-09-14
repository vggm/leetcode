class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        triangle = []
        
        for i in range(rowIndex+1):
            triangle.append([1] * (i+1))
            for j in range(1,i):
                triangle[i][j] = triangle[i-1][j-1]+triangle[i-1][j]
        
        return triangle[-1]
    
    
print(Solution().getRow(3))