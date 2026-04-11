class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_t = []

        for i, pos in enumerate(position):
            t = (target - pos)/speed[i]
            pos_t.append((pos, t))
        
        pos_t = sorted(pos_t)
        
        for i, (pos,t) in enumerate(reversed(pos_t)):
            idx = len(position) - 1 - i
            if stack and t <= stack[-1][0]:
                stack[-1].append(t)
            else:
                stack.append([t])

        return len(stack)