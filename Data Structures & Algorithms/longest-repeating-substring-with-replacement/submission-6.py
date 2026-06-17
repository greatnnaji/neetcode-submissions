class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        maxLen = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(count.values())

            lenLeft = (r - l + 1) - maxf

            while lenLeft > k:
                count[s[l]] -= 1
                l += 1
                maxf = max(count.values())
                lenLeft = (r - l + 1) - maxf

            maxLen = max(maxLen, r - l + 1)

        return maxLen