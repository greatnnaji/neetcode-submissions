class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums_hashmap = {} # causes it to be a set

        nums_hashmap = dict()

        for index,value in enumerate(nums):
            nums_hashmap[value] = index

        print(nums_hashmap)
        
        for index,value in enumerate(nums):
            j = index
            difference = target - value
            print(difference)
            if difference in nums_hashmap:
                i = nums_hashmap[difference]
                if i != j:
                    if i < j:
                        return [i,j]
                    else:
                        return [j,i]


        return []
            


        