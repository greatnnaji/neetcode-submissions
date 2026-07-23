class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        r = 0
        count = {}
        max_count = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(max_count, count.get(s[r]))

            if (r - l + 1) - max_count <= k:
                longest = max(longest, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

            r += 1
        
        return longest