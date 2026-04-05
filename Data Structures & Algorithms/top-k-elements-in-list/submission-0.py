from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])
        
        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1): # start len(bucket)-1, stop at 0, count down -1 (step), stop = 0 same as while stop > 0
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
