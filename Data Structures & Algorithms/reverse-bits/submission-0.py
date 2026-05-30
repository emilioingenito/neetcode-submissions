class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:].zfill(32)[::-1]
        return int(''.join(s), 2)
    