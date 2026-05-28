class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(curr, i):
            if i == len(word):
                return curr.endOfWord
            
            if word[i] == ".":
                for k, v in curr.children.items():
                    if dfs(v, i+1):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False
                return dfs(curr.children[word[i]], i+1)
            
        return dfs(self.root, 0)
        
