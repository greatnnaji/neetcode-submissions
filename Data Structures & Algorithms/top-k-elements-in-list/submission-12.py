class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hashmap = {}

        for index,value in enumerate(nums):
            if value in nums_hashmap:
                nums_hashmap[value] += 1
            else:
                nums_hashmap[value] = 1

        print(nums_hashmap)
        
        nums_length = len(nums) + 1 # TBU

        bucket = [0] * nums_length

        print(bucket)

        for value,occ in nums_hashmap.items():
            if bucket[occ] == 0:
                bucket[occ] = [value]
            else:
                bucket[occ].append(value)

        print(bucket)        

        top_k = []

        for index,item in enumerate(reversed(bucket)):
            if isinstance(item, list):
                for value in item:
                    if len(top_k) < k:
                        top_k.append(value)
        
        print(top_k)

        return top_k