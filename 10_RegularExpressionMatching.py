

class Solution:
  
  def isMatch( self, target: str, pattern: str ) -> bool:

    def backtracking( i=0, j=0, temp={} ) -> bool:
      answer = False
      node = (i,j)
      
      if temp.get(node) is not None:
        return temp[node]
      
      if j == len(pattern): return i == len(target)
      
      match = i < len(target) and pattern[j] in ['.', target[i]]
      
      if j < len(pattern)-1 and pattern[j+1] == '*':
        if match:
          answer = backtracking(i+1, j)
        if not answer: 
          answer = backtracking(i, j+2)
      
      if match and not answer:
        answer = backtracking(i+1,j+1)
      
      temp[node] = answer
          
      return answer
  
    return backtracking()
  

solution = Solution()

res = solution.isMatch( 'aa', 'a' )
print(res)

res = solution.isMatch( 'aa', 'a.' )
print(res)

res = solution.isMatch( 'aaaaaaaaaaa', 'a*' )
print(res)

res = solution.isMatch( 'cb', 'a*b' )
print(res)

res = solution.isMatch( 'ab', '.*' )
print(res)

res = solution.isMatch( '', 'a*' )
print(res)

res = solution.isMatch( '', '.' )
print(res)

res = solution.isMatch( 'aab', 'c*a*b' )
print(res)
