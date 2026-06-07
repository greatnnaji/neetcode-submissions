class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict()
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1
        
        for num, occ in num_dict.items():
            buckets[occ].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
            if len(res) == k:
                return res