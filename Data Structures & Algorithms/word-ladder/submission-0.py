from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = self.build(wordList + [beginWord])
        queue, ladder, visited = deque([beginWord]), 0, set([beginWord])

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return ladder + 1
                for node in graph[word]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
            ladder += 1

        return 0
    

    def build(self, wordList: List[str]) -> dict:
        graph = defaultdict(list)
        for index, word in enumerate(wordList):
            for other_word in wordList[index+1:]:
                if self.is_neighbor(word, other_word):
                    graph[word].append(other_word)
                    graph[other_word].append(word)
        return graph
    

    def is_neighbor(self, a: str, b: str) -> bool:
        differencies = 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                differencies += 1
            if differencies > 1:
                return False
        return differencies == 1