class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        maxLen = 0
        l = 0

        for r in range(len(s)):
            while s[r] in uniq:
                print(uniq)
                uniq.remove(s[l])
                l += 1
            uniq.add(s[r])
            maxLen = max(maxLen, len(uniq))

        return maxLen

