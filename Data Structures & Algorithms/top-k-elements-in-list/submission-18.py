from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]

        for val, occ in count.items():
            freq[occ].append(val)
                
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
            
        
        return []


