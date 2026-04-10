class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []

        rev_temp = list(reversed(temperatures))

        for i, t in enumerate(rev_temp):
            idx = len(rev_temp) - 1 - i

            while stack and t >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                result.append(stack[-1] - idx)
            else:
                result.append(0)

            stack.append(idx)

            print("stack: ", stack)
            print("result: ", result)

        # reverse result at end
        result = list(reversed(result))           

        return result