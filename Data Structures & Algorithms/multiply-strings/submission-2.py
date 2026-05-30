class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 =='0' or num2 == '0':
            return '0'

        long, short = (num1, num2) if len(num1) > len(num2) else (num2, num1)
        ans = [0] * (len(num1) + len(num2))
        ans_pos = len(ans) - 1

        for a in reversed(short):
            carry, index = 0, ans_pos
            for c in reversed(long):
                temp = int(c) * int(a) + carry + ans[index]
                ans[index], carry = temp % 10, temp // 10
                index -= 1
            if carry:
                ans[index] = carry
            ans_pos -= 1
        
        return ''.join([str(c) for c in ans]).lstrip('0')