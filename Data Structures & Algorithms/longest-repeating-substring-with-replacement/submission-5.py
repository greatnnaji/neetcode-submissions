class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        maxf = 0
        l = 0
        count = dict()

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            if r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1 # check might be a count.remove(s[l])
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen
        
            
