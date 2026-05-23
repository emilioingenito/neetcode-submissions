class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, operators = [], '-+*/'
        for n in tokens:
            print(stack)
            if n in operators:
                second = stack.pop()
                first = stack.pop()
                value = self.evaluate(first, second, n)
                stack.append(value)
            else:
                stack.append(int(n))
        
        print(stack)
        return stack[0]

    
    def evaluate(self, first: int, second: int, operator: str) -> int:
        if operator == '+':
            return first + second

        elif operator == '-':
            return first - second

        elif operator == '*':
            return first * second

        elif operator == '/':
            return int(first/second)
        
        raise Exception('Not recognized operator')

        