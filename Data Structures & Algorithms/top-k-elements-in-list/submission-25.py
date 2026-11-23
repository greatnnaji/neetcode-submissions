from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # map of num:occ

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, occ in count.items():
            buckets[occ].append(num)

        res = []

        for item in range(len(buckets) - 1, 0, -1):
            if buckets[item] != []:
                for val in buckets[item]:
                    res.append(val)
                    if len(res) == k:
                        return res


        return []