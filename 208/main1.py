class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word: str) -> None:
        node = self
        for c in word:
            c = ord(c) - ord('a')
            if not node.children[c]:
                node.children[c] = Trie()
            node = node.children[c]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self
        for c in word:
            c = ord(c) - ord('a')
            if not node.children[c]:
                return False
            node = node.children[c]
        return node.isEnd


    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            c = ord(c) - ord('a')
            if not node.children[c]:
                return False
            node = node.children[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
