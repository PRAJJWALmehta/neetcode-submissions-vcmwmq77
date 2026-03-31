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

        self.res = max(self.res, left + root.val + right)

        return max(0, root.val + max(left, right))


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        self.traverse(root)

        return int(self.res)


        