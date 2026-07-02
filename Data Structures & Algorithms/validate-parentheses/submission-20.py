class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')' : '(' , '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                last = stack.pop() if stack else "!"

                if closeToOpen[c] != last:
                    return False

        return not stack                    

                
                    