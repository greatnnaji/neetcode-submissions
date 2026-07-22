class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        longest = 0
        l = 0
        r = 0

        while r < len(s):
            while s[r] in uniq:
                uniq.discard(s[l])
                l += 1
            
            uniq.add(s[r])
            longest = max(longest, len(uniq))
            r += 1
        
        return longest
        
            