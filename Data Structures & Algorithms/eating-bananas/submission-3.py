import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) == 1:
        #     return math.ceil(piles[0]/h)

        start = 1
        end = max(piles)

        min_k = end

        while start <= end:
            k = (end - start)//2 + start
            sub_hrs = 0
            for val in piles:
                sub_hrs += math.ceil(val/k)
            # print("sub_hrs: ", sub_hrs)
            
            if sub_hrs <= h:
                min_k = min(min_k, k)
                end = k - 1
                # print("end: ", end)
            else:
                start = k + 1
                # print("start: ", start)

        print(min_k)



        return min_k
