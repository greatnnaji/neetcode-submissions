from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # dict of val to occ
        arr = [0] * (len(nums) + 1)

        for val in count:
            arr[count[val]] = [] # put empty array at occ loc

        for val in count:
            arr[count[val]].append(val)

        num = 0
        output = []
        for val in reversed(arr):
            idx = 0
            if val != 0:
                while num < k and idx < len(val):
                    output.append(val[idx])
                    num += 1
                    idx += 1
                    
        return output