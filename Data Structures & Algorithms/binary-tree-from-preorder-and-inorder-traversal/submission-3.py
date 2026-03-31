# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _dfs(self, l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        
        root = TreeNode(preorder[self.preIdx])
        self.preIdx += 1
        mid = self.findIdx[root.val]
        root.left = self._dfs(l, mid-1)
        root.right = self._dfs(mid+1, r)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIdx = 0
        self.findIdx = {val: idx for idx, val in enumerate(inorder)}

        return self._dfs(0, len(inorder)-1)
        