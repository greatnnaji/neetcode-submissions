from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        count = [[] for _ in range(len(nums) + 1)]

        for val, occ in freq.items():
            count[occ].append(val)

        res = []
        for i in range(len(nums), 0, -1):
            for val in count[i]:
                if len(res) == k:
                    return res
                res.append(val)

        return res