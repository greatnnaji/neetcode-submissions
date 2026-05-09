class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        max_occ = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_occ = max(max_occ, count[s[r]])

            while (r - l + 1) - max_occ > k: # window len - max_occ > k
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            
            res = max(res, r - l + 1) 
        
        return res
