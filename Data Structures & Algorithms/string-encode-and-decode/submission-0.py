class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        hello world
        hello5world5
        h5i8 38943
        hellohello hellohello
        5hello5hello
        1|1|1| 3287 |1|1|1
        6|1|1|1|4|32876||1|1|1
        '''
        encoded = [str(len(string)) + '|' + string for string in strs]
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        idx = 0

        while idx < len(s):
            current, length = [], []
            while idx < len(s) and s[idx].isnumeric():
                length.append(s[idx])
                idx += 1
            nLength = int(''.join(length))
            current = s[idx+1:idx+1+nLength]
            decoded.append(current)
            idx = idx + 1 + nLength
        
        return decoded
