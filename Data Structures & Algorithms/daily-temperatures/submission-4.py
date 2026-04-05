class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_stack = []
        result = []

        reverse_temp = list(reversed(temperatures))
        print(reverse_temp)

        for i, temp in enumerate(reverse_temp):
            print("index: ", i)
            if len(min_stack) == 0:
                result.append(0)
                min_stack.append(i)
                print("minstack1: ", min_stack)
            else:
                while temp >= reverse_temp[min_stack[-1]]:
                    min_stack.pop()
                    print("popping...")
                    if len(min_stack) == 0:
                        break
                print("minstack2: ", min_stack)
                if len(min_stack) == 0:
                    result.append(0)
                    min_stack.append(i)
                else:
                    result.append(abs(i - min_stack[-1]))
                    min_stack.append(i)
                print("minstack3: ", min_stack)
        
        result = list(reversed(result))

        print(result)

        return result

        # reverse result before return

                