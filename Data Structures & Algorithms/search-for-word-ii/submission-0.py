class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word: str):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isEnd = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, node, word):
            if (
                i < 0 or
                i >= ROWS or 
                j < 0 or 
                j >= COLS or
                (i, j) in visited or 
                board[i][j] not in node.children 
                ):
                return
            
            visited.add((i, j))

            node = node.children[board[i][j]]
            word += board[i][j]

            if node.isEnd:
                res.add(word)
                node.isEnd = False
                
            for dr, dc in directions:
                r = i + dr
                c = j + dc
                dfs(r, c, node, word)
            
            visited.remove((i, j))
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")
        
        return list(res)


        

