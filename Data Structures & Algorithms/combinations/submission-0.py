class Solution:
    def combine(self, N: int, K: int) -> List[List[int]]:
        ans = []

        def backtrack(n, k, partial):
            if k == 0:
                ans.append(partial[:])
                return
            for i in range(n, N+1):
                partial.append(i)
                backtrack(i+1, k-1, partial)
                partial.pop()


        backtrack(1, K, [])
        return ans