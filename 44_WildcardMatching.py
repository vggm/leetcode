class Solution:
  
  def isMatch( self, target: str, pattern: str ) -> bool:

    def backtracking( i=0, j=0, last=None, temp={} ) -> bool:
      answer = False
      node = (i,j)
      
      if temp.get(node) is not None:
        return temp[node]
      
      if j == len(pattern): return i == len(target)
      
      match = i < len(target) and pattern[j] in ['?', target[i]]
      
      if pattern[j] == '*':
        answer = backtracking(i+1, j)
      
      if match and not answer:
        answer = backtracking(i+1,j+1)
      
      temp[node] = answer
          
      return answer
  
    return backtracking()
  

solution = Solution()

res = solution.isMatch( 'aa', 'a' )
print(res)

res = solution.isMatch( 'aa', '*' )
print(res)

res = solution.isMatch( 'cb', '?a' )
print(res)