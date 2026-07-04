class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        mon_stack = []

        for i, t in enumerate(reversed(temperatures)):
            while mon_stack and t >= mon_stack[-1][0]:
                    mon_stack.pop()

            if not mon_stack:
                mon_stack.append((t, i))
                res.append(0)
            else:
                res.append(i - mon_stack[-1][1])
                mon_stack.append((t, i))                

        return list(reversed(res))