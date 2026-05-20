class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if stack and t in op:
                r = int(stack.pop())
                l = int(stack.pop())
                if t == "+":
                    total = l + r
                elif t == "-":
                    total = l - r
                elif t == "*":
                    total = l * r
                else:
                    total = int(l/r)
                
                stack.append(total)
            else:
                stack.append(int(t))
        
        return stack[0]

