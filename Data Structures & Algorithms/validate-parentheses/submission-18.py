class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in closeToOpen:
                top = stack.pop() if stack else "%"

                if closeToOpen[c] != top:
                    return False
            else:
                stack.append(c)
        
        return not stack

