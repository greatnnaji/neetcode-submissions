class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stack.append((start, h))
        
        print(stack)
        for i, (index, h) in enumerate(stack):
            maxArea = max(maxArea, (len(heights) - index) * h)
        
        print(maxArea)

        return maxArea

            
