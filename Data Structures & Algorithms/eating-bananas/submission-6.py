import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        i = 1
        minHrs = k

        while i <= k:
            mid = (k + i)//2
            total_hrs = 0
            for val in piles: 
                total_hrs += math.ceil(val/mid)
                        
            if total_hrs <= h:
                minHrs = min(minHrs, mid)
                k = mid - 1
            else:
                i = mid + 1
        
        return minHrs


