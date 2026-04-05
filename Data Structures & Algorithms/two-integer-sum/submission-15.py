class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()

        for index,num in enumerate(nums):
            hashMap[num] = index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                if hashMap[diff] != index:
                    return [index, hashMap[diff]]

        return []