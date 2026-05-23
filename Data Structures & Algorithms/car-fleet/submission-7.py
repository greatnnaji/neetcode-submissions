class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time it takes a car to reach dest is (target - pos) / spd
        pos_dict = dict(zip(position, speed))
        pos_dict = {k: pos_dict[k] for k in sorted(pos_dict)}
        stack = []

        for pos, spd in reversed(list(pos_dict.items())):
            t = (target - pos) / spd
            stack.append(t)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
