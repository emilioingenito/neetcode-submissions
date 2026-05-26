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

    '''
    # BFS Approach
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
    '''

    # DFS Approach
    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return '*' in node
            
            if word[index] in node:
                return dfs(node[word[index]], index+1)
            
            found = False
            if word[index] == '.':
                found = any(dfs(node[value], index+1) for value in node if value != '*')
            return found

        return dfs(self.trie, 0)
