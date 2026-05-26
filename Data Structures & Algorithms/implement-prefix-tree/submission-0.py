class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        node = self.trie
        for n in word:
            if n not in node:
                node[n]= {}
            node = node[n]
        node['*'] = {}
        return

    
    def searchNode(self, word: str) -> dict:
        node = self.trie
        for n in word:
            if n not in node:
                return {}
            node = node[n]
        return node


    def search(self, word: str) -> bool:
        return '*' in self.searchNode(word)

        
    def startsWith(self, prefix: str) -> bool:
        return self.searchNode(prefix) != {}

        
        