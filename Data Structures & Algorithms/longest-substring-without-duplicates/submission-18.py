class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        unique = set()
        l = 0
        
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            maxLen = max(maxLen, len(unique))

        return maxLen
