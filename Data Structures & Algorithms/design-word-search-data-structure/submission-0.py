class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.word
            
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            if c in node.children:
                return dfs(node.children[c], i + 1)
            return False
        
        return dfs(self.root, 0)