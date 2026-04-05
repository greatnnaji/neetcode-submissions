class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1: return int(tokens[0])
        for c in tokens:
            if c == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) - int(second))
                print("on subtract: ", stack)
            elif c == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif c == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(int(first)/int(second)))
                print("on div: ", stack)
            else:
                stack.append(c)
        
        return stack.pop()
