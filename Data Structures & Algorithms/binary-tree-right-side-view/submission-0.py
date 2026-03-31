# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()

        if root:
            q.append(root)
        
        while q:
            count = len(q)
            visibleNode = 0

            while count:
                node = q.popleft()
                count -= 1
                visibleNode = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(visibleNode)
        
        return res
                


        