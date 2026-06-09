class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        freq_dict = dict()

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        for num, occ in freq_dict.items():
            freq[occ].append(num)

        res = []

        for i in range(len(nums), 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

