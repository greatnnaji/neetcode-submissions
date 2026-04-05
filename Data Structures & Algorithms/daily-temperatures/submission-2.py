class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        output = []



        for index, temp in enumerate(reversed(temperatures)):
            temp_idx = len(temperatures) - 1 - index

            if len(mon_stack) == 0:
                output.append(0)
                mon_stack.append(temp_idx)
            else:
                if len(mon_stack) != 0:
                    while temp >= temperatures[mon_stack[-1]]:
                        mon_stack.pop()
                        if len(mon_stack) == 0:
                            break
                    
                    if len(mon_stack) == 0:
                        output.append(0)
                    else:
                        output.append(abs(temp_idx - mon_stack[-1]))

                    mon_stack.append(temp_idx)
            
        # reverse output

        # print("mon_stack: ", mon_stack)
        # print("output: ")
        # print(list(reversed(output)))

        output = list(reversed(output))

        return output