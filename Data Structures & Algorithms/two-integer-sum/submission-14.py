class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}

        for index,value in enumerate(nums):
            nums_hashmap[value] = index

        # print(nums_hashmap)

        for index,value in enumerate(nums):
            diff_value = target - nums[index]

            if diff_value in nums_hashmap and nums_hashmap[diff_value] != index:
                if nums_hashmap[diff_value] < index:
                    print([nums_hashmap[diff_value], index])
                    return [nums_hashmap[diff_value], index]
                else:
                    print([index, nums_hashmap[diff_value]])
                    return [index, nums_hashmap[diff_value]]

        return []