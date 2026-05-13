from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        countS1 = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if countS1 == window_count:
            return True

        for r in range(len(s1), len(s2)):
            window_count[s2[r]] += 1 # check if fails

            start_idx = r - len(s1)
            left_start = s2[start_idx]
            window_count[left_start] -= 1

            if s2[start_idx] == 0:
                del s2[left_start]
            
            if countS1 == window_count:
                return True

        return False