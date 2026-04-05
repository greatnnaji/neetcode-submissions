class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need to know frequency so need hashmap (ex. key: 1, value: 3 (occurence))
        # bucket sort -> O(n) since "any order"
        # single item can appear max of n times

        num_hashmap = dict()
        for index,value in enumerate(nums):
            if value not in num_hashmap:
                num_hashmap[value] = 1
            else:
                num_hashmap[value] += 1
        
        print(num_hashmap)

        nums_length = len(nums) + 1 
        # + 1 needed for edge cases using bucket[value], if value = len(nums) then index out of bounds

        bucket = [0] * nums_length # implement as array of arrays

        for key,value in num_hashmap.items():
            print(value)
            if bucket[value] == 0:
                bucket[value] = [key]
                print(bucket)
            else:
                bucket[value].append(key)

        print(bucket)
        
        # read bucket from back to front

        top_k = []

        for index,item in enumerate(reversed(bucket)):
            if item != 0:
                for value in item:
                    if len(top_k) < k:
                        top_k.append(value)
        
        print(top_k)

        return top_k
