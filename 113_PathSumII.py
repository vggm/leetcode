
class Node:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
  

class Solution:
  def pathSum(self, root: Node, targetSum: int) -> list[list[int]]:
    if not root: return []
    
    solution = []
    def dps ( root: Node, total=0, parcial:list=[] ) -> None:
      parcial.append(root.val)
      
      if not root.left and not root.right: # is leaf
        if (total + root.val) == targetSum:
          solution.append(parcial.copy())
          
      else:
        if root.left:
          dps(root.left, total+root.val, parcial)
          
        if root.right:
          dps(root.right, total+root.val, parcial)
      
      parcial.pop()
      
      
    dps( root )
    return solution
  
