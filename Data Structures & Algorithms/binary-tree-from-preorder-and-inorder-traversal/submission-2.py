# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, l: int, r: int):
        if l > r:
            return None
        
        root = TreeNode(preorder[self.preIdx])
        self.preIdx += 1
        mid = self.findIdx[root.val]
        root.left = self.dfs(l, mid-1)
        root.right = self.dfs(mid+1, r)
        return root
        

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.findIdx = {}
        self.preIdx = 0

        for i, val in enumerate(inorder):
            self.findIdx[val] = i
        
        return self.dfs(0, len(inorder)-1)
        
        