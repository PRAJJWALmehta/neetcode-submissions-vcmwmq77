# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        left = self.traverse(root.left)
        self.count -= 1
        if not self.count:
            return root.val
        right = self.traverse(root.right)

        return max(left, right)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k

        return self.traverse(root)
        