class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxA = 0

        while l < r:
            minBar = min(heights[l], heights[r])
            width = r - l
            
            maxA = max(maxA, minBar * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxA

