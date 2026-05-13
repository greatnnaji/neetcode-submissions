class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        count = set()

        for r in range(len(s)):
            if s[r] in count:
                while s[r] in count:
                    count.remove(s[l])
                    l += 1
            count.add(s[r])
            maxLen  = max(maxLen, len(count))
        
        return maxLen
