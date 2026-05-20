class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = dict()

        brackets['('] = ')'
        brackets['{'] = '}'
        brackets['['] = ']'

        i = 0
        while i < len(s):
            if stack and s[i] not in brackets:
                if stack[-1] in brackets and brackets[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            print(stack)
            i += 1
        
        print(len(stack))
        print(stack)
    
        return len(stack) == 0