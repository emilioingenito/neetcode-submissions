class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        x = x if n >= 0 else 1/x
        for _ in range(abs(n)):
            ans *= x

        return ans