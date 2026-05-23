class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time it takes a car to reach dest is (target - pos) / spd
        pos_dict = dict(zip(position, speed))
        pos_dict = {k: pos_dict[k] for k in sorted(pos_dict)}

        stack = []
        fleet = 1

        for pos, spd in reversed(list(pos_dict.items())):
            t = (target - pos) / spd
            print(pos, spd)
            print("time: ", t)
            
            if stack:
                if t > stack[-1]:
                    stack.pop()
                    stack.append(t)
                    fleet += 1
            else:
                stack.append(t)
            
            print(stack)
            print(fleet)
        
        return fleet
