class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie, words = self.build(words), []
        N, M = len(board), len(board[0])

        def dfs(x: int, y: int, node: dict, visited: set) -> str:
            if '*' in node:
                words.append(node['*'])
                del node['*']
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] in node and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs(nx, ny, node[board[nx][ny]], visited)
                    visited.remove((nx, ny))

        for x in range(N):
            for y in range(M):
                if board[x][y] in trie:
                    dfs(x, y, trie[board[x][y]], set([(x,y)]))
        return words


    def build(self, words: List[str]) -> dict:
        trie = {}
        for word in words:
            self.add(trie, word)
        return trie
    

    def add(self, trie: dict, word: str) -> None:
        node = trie
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['*'] = word
        return