class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # holds (start idx, height)

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # calc max area, check cur max area
                # pop
                index, height = stack.pop()
                curArea = height * (i - index)
                if curArea > maxArea:
                    maxArea = curArea
                start = index
            
            stack.append((start,h))

        for idx,h in stack:
            curArea = h * (len(heights) - idx)
            if curArea > maxArea:
                maxArea = curArea
        
        print("FINAL MAXAREA: ", maxArea)
        
        
        return maxArea
        
