class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i, j = 0, 1
        maxLen = 0

        if s == "": return 0
        if len(s) == 1: return 1

        uniq = dict()
        uniq[s[i]] = i

        while j < len(s):
            print(uniq)
            if s[j] not in uniq:
                uniq[s[j]] = j
            else:
                i = uniq[s[j]] + 1
                uniq = dict()
                
                temp_i = i
                while temp_i <= j:
                    uniq[s[temp_i]] = temp_i
                    temp_i += 1
                
            maxLen = max(maxLen, len(uniq))
            j += 1
        
        print(maxLen)

        return maxLen