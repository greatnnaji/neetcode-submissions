class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_stack = []
        result = []

        reverse_temp = list(reversed(temperatures))

        for i, temp in enumerate(reverse_temp):
            if len(min_stack) == 0:
                result.append(0)
                min_stack.append(i)
            else:
                while temp >= reverse_temp[min_stack[-1]]:
                    min_stack.pop()
                    if len(min_stack) == 0:
                        break
                if len(min_stack) == 0:
                    result.append(0)
                    min_stack.append(i)
                else:
                    result.append(abs(i - min_stack[-1]))
                    min_stack.append(i)
        
        result = list(reversed(result))

        # reverse result before return

        return result

                