class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            dist = r - l
            if heights[l] > heights[r]:
                newA = dist * heights[r]
                if maxA < newA: maxA = newA
                r -= 1
            else:
                newA = dist * heights[l]
                if maxA < newA: maxA = newA
                l += 1
        
        return maxA




            
        