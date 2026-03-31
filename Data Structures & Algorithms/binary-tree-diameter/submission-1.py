# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        maxLen = max(left+right, max(left, right))
        self.diameter = max(self.diameter, maxLen)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = float('-inf')
        self.traverse(root)

        return int(self.diameter)
        