class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        lwc = r
        wgt = []

        while l <= r:
            mid = (l + r)//2

            for w in weights:
                if wgt and wgt[-1] + w <= mid:
                    wgt[-1] += w
                else:
                    wgt.append(w)
            
            if len(wgt) > days:
                l = mid + 1
            else:
                lwc = min(lwc, mid)
                r = mid - 1

            wgt = []
        
        return lwc
