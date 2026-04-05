class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        output = []

        reversed_temp = list(reversed(temperatures))
    
        for index, temp in enumerate(reversed_temp):
            print("temp: ", temp)
            if len(mon_stack) == 0:
                output.append(0)
                mon_stack.append(index)
                # print("output: ", output)
                # print("mon_stack: ", mon_stack)
            else:
                print("mon_stack: ", mon_stack)
                if temp < reversed_temp[mon_stack[-1]]:
                    print("temp less...")
                    # print("index: ", index)
                    # print("mon_stack[-1]:", mon_stack[-1])
                    output.append(abs(index - mon_stack[-1]))
                    mon_stack.append(index)
                else:
                    print("temp greater...")
                    print("mon_stack: ", mon_stack)
                    while temp >= reversed_temp[mon_stack[-1]]:
                        print(mon_stack[-1])
                        print("temperatures[mon_stack[-1]]: ", reversed_temp[mon_stack[-1]])
                        print("popping...")
                        mon_stack.pop()
                        if len(mon_stack) == 0: 
                            # output.append(0)
                            break
                    print("mon_stack: ", mon_stack)
                    if len(mon_stack) == 0: 
                        output.append(0)
                    else:
                        print("GREATER")
                        print("index: ", index)
                        print("mon_stack[-1]:", mon_stack[-1])
                        output.append(abs(index - mon_stack[-1]))

                    mon_stack.append(index)
                    print("mon_stack: ", mon_stack)

                print("output: ", output)
        
        print("output: " , output)
        
        # reverse output before return

        return list(reversed(output))