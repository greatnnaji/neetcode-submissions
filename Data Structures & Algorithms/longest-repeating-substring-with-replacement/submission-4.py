class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLen = 0
        count = dict()
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            print("length: ", r - l + 1)
            print("maxf: ", maxf)
            if (r - l + 1) - maxf <= k:
                maxLen = max(maxLen, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

            
            print(maxLen)
        
        return maxLen
