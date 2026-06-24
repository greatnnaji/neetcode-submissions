import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minK = max(piles)

        while l <= r:
            mid = (l + r) // 2

            curHr = 0
            for p in piles:
                curHr += math.ceil(p/mid)
            
            if curHr > h:
                l = mid + 1
            elif curHr <= h:
                minK = min(minK, mid)
                r = mid - 1
        
        return minK