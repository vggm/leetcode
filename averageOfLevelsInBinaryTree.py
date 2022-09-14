# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # def averageOfLevels(self, root: TreeNode) -> list[float]:
        
    #     valPerLevel   = []
    #     nodesPerLevel = []
    #     def search(root: TreeNode, lvl = 0):
    #         if root is not None:
    #             if len(valPerLevel) < lvl+1:
    #                 valPerLevel.append(root.val)
    #                 nodesPerLevel.append(1)
    #             else:
    #                 valPerLevel[lvl] += root.val
    #                 nodesPerLevel[lvl] += 1
                
    #             search(root.left,lvl+1)
    #             search(root.right,lvl+1)
        
    #     search(root)
        
    #     for i in range(len(valPerLevel)):
    #         valPerLevel[i] = valPerLevel[i] / nodesPerLevel[i]
        
    #     return valPerLevel
    
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        if not root:
            return []
        
        res = []
        q = [root]
        
        while q:
            size = len(q)
            valPerLevel = 0
            
            for i in range(size):
                curr = q.pop(0)
                valPerLevel+=curr.val
                
                q.append(curr.right) if curr.right else None
                q.append(curr.left) if curr.left else None
            
            res.append(valPerLevel/size)
        
        return res
    
        
root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(Solution().averageOfLevels(root))