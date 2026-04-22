import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        i = 1
        minHrs = k

        while i <= k:
            print("i-0: ", i)
            print("k-0: ", k)
            mid = (k + i)//2
            hrs = 0
            for val in piles: 
                hrs += math.ceil(val/mid)
                        
            if hrs <= h:
                minHrs = min(minHrs, hrs)
                k = mid - 1
            else:
                i = mid + 1
            print("i: ", i)
            print("k: ", k)
        
        print(minHrs)

        return i


