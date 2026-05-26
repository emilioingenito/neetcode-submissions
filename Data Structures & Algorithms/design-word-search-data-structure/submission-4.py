from collections import deque
class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node['*'] = {}


    def search(self, word: str) -> bool:
        queue = deque([(0, self.trie)])
        while queue:
            index, node = queue.popleft()
            if index == len(word):
                return '*' in node
            char = word[index]
            if char in node:
                queue.append((index+1, node[char]))
            elif char == '.':
                queue.extend([(index+1, node[value]) for value in node if value != '*'])
        return False
        
