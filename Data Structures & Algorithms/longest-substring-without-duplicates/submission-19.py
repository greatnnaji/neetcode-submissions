class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        uniq = set()
        maxLen = 0

        for r in range(len(s)):
            if s[r] in uniq:
                while s[r] in uniq:
                    uniq.remove(s[l])
                    l += 1
            uniq.add(s[r])
            maxLen = max(maxLen, len(uniq))

        return maxLen