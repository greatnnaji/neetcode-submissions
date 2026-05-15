class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        min_k = max(piles)
        l = 1

        while l <= r:
            k_mid = (r + l)//2
            sub_t = 0

            for pile in piles:
                sub_t += math.ceil(pile/k_mid)
            
            if sub_t <= h:
                min_k = min(min_k, k_mid)
                r = k_mid - 1
            elif sub_t > h:
                l = k_mid + 1
        
        return min_k
            


