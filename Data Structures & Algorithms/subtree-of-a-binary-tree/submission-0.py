# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        r = root
        q = deque()
        if r:
            q.append(r)
        
        while q:
            count = len(q)

            while count:
                node = q.popleft()
                count -= 1
                if node.val == subRoot.val:
                    if self.isSameTree(node, subRoot):
                        return True
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return False

        
        