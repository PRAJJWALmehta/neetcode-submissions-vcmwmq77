# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                res.append("N")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        idx = 0
        nodes = data.split(",")


        def dfs() -> Optional[TreeNode]:
            nonlocal idx
            if idx > len(nodes)-1 or nodes[idx] == 'N':
                idx += 1
                return None
            
            node = TreeNode(nodes[idx])
            idx += 1
            
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()


