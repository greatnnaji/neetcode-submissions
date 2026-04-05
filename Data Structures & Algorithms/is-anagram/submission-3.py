from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # seen = {}

        # for char in s:
        #     if char not in seen:
        #         seen[char] = 1
        #     else:
        #         seen[char] += 1 

        # newSeen = {}
        # for char in t:
        #     if char not in seen:
        #         return False
        #     elif char not in newSeen:
        #         newSeen[char] = 1
        #     else:
        #         newSeen[char] += 1
        
        # return seen == newSeen

        ss = Counter(s)
        tt = Counter(t)

        return ss == tt
