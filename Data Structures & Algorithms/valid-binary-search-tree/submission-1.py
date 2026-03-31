# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validateBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not self.validateBST(root.left):
            return False
        
        if root.val <= self.lastVal:
            return False
        self.lastVal = root.val

        if not self.validateBST(root.right):
            return False
        
                    
        
        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lastVal = float('-inf')

        return self.validateBST(root)