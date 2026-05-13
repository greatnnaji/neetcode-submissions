from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        countS1 = Counter(s1)
        
        for l in range(len(s2)):
            if s2[l] in countS1:
                r = l + len(s1) - 1
                temp_str = ""
                while r < len(s2) and l <= r:
                    temp_str += s2[l]
                    l += 1
                tempCount = Counter(temp_str)

                if countS1 == tempCount:
                    return True
        
        return False
                
