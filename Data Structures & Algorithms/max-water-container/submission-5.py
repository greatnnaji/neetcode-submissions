class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxA = 0

        while l < r:
            minBar = min(heights[l], heights[r])
            width = r - l
            if minBar == heights[l]:
                l += 1
            elif minBar == heights[r]:
                r -= 1
            
            maxA = max(maxA, minBar * width)

        return maxA

