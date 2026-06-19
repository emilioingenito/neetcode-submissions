class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        wildcard = []
        for i, c in enumerate(s):
            match c:
                case '(':
                    stack.append(i)
                case ')':
                    if stack: stack.pop()
                    elif wildcard: wildcard.pop()
                    else: return False
                case '*':
                    wildcard.append(i)
        while stack:
            if not wildcard or stack.pop() > wildcard.pop():
                return False
        return True