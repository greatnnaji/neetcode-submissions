class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_h = 0

        while l < r:
            length = min(heights[l], heights[r])
            width = r - l

            max_h = max(max_h, length * width)

            if length == heights[l]:
                l += 1
            else:
                r -= 1

        return max_h

