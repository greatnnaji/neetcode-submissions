class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0: return False

        closing = set()
        closing.add(')')
        closing.add(']')
        closing.add('}')

        opening = set()
        opening.add('(')
        opening.add('[')
        opening.add('{')

        start = 0
        end = len(s) - 1
        if s[start] in closing:
            return False

        if s[end] in opening:
            return False

        if len(s) == 1:
            return False

        expected_map = dict()

        for char in s:
            if char == '[': expected_map['['] = ']'
            elif char == '(': expected_map['('] = ')'
            else:
                expected_map['{'] = '}'

        stack = []

        while start < len(s):
            while s[start] in opening:
                stack.append(s[start])
                start += 1

            print(stack)
            print("s[start]: ", s[start])
            expected_s = expected_map[stack[-1]]
            print("expected_s: ", expected_s)
            if s[start] != expected_s: 
                return False
            else:
                print("popping...")
                stack.pop()
                print(stack)
                start += 1

        if len(stack) > 0: return False
                            
        return True
        