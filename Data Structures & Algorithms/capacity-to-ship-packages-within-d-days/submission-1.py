class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        lwc = r = sum(weights)

        while l <= r:
            mid = (l + r)//2

            running_sum = 0
            cur_days = 1

            for w in weights:
                if w + running_sum <= mid:
                    running_sum += w
                else:
                    running_sum = w
                    cur_days += 1
            
            if cur_days > days:
                l = mid + 1
            else:
                lwc = min(lwc, mid)
                r = mid - 1
        
        return lwc


