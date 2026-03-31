# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: TreeNode, maxVal: int) -> None:
        if not root:
            return
        
        if maxVal <= root.val:
            self.goodNodes += 1
        
        self.traverse(root.left, max(maxVal, root.val))
        self.traverse(root.right, max(maxVal, root.val))
        


    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0

        self.traverse(root, root.val)

        return self.goodNodes
        