class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = dict()

        brackets['('] = ')'
        brackets['{'] = '}'
        brackets['['] = ']'

        i = 0
        while i < len(s):
            if stack and stack[-1] in brackets and s[i] not in brackets and brackets[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
    
        return len(stack) == 0