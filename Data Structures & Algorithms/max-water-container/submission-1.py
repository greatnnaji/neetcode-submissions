class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            if heights[left] < heights[right]:
                length = heights[left]
                left += 1
            else:
                length = heights[right]
                right -= 1
            
            cur_area = length * width

            if cur_area > max_area:
                max_area = cur_area
        
        # print(max_area)

        return max_area
            
            
            