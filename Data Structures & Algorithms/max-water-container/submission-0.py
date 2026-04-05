class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights) - 1

        max_area = 0

        while start < end:
            min_height = min(heights[start], heights[end])
            print("min_height: ", min_height)

            cur_area = (end-start) * min_height
            print("cur_area: ", cur_area)

            if cur_area > max_area:
                max_area = cur_area

            if min_height == heights[start]:
                start += 1
            else:
                end -= 1
        
        print(max_area)

        return max_area
            
            

        