class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        output = []

        # goal/trick of monotic stack is to keep an increasing/descreasing list
        # in this case decreasing

        reversed_temp = list(reversed(temperatures))
    
        for index, temp in enumerate(reversed_temp):
            if len(mon_stack) == 0:
                output.append(0)
                mon_stack.append(index)
            else:
                if temp < reversed_temp[mon_stack[-1]]:
                    output.append(abs(index - mon_stack[-1]))
                    mon_stack.append(index)
                else:
                    while temp >= reversed_temp[mon_stack[-1]]:
                        mon_stack.pop()
                        if len(mon_stack) == 0: 
                            break
                    if len(mon_stack) == 0: 
                        output.append(0)
                    else:
                        output.append(abs(index - mon_stack[-1]))

                    mon_stack.append(index)
                
        # reverse output before return

        return list(reversed(output))