class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # holds (start idx, height)

        for i,h in enumerate(heights):
            # print(i)
            start = i
            while stack and stack[-1][1] > h:
                # calc max area, check cur max area
                # pop
                start = stack[-1][0]
                curArea = stack[-1][1] * (i - stack[-1][0])
                if curArea > maxArea:
                    maxArea = curArea
                stack.pop()
            
            stack.append((start,h))

        for idx,h in stack:
            curArea = h * (len(heights) - idx)
            if curArea > maxArea:
                maxArea = curArea
                
        
        return maxArea
        
