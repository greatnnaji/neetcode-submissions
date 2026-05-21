class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        result = []

        for i, temp in enumerate(reversed(temperatures)):
            index = len(temperatures) - i - 1
            
            while mon_stack and temp >= temperatures[mon_stack[-1]]:
                mon_stack.pop()

            if mon_stack:
                result.append(mon_stack[-1] - index)
            else:
                result.append(0)

            mon_stack.append(index)
        
        return list(reversed(result))