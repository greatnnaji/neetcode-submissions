import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1)
        right = []
        right.append(1)

        # get everything to the left of index i -> max product to left of i
        for i, value in enumerate(nums[:-1]):
            left.append(value * left[-1])

        # get everything to the right of index i -> max product to right of i
        for i,value in reversed(list(enumerate(nums[1:]))): # reversed to go from right to left excluding last element
            right.insert(0, value * right[0])
        
        # arr1 = np.array(left)
        # arr2 = np.array(right)

        # result_arr = np.multiply(arr1,arr2)

        result_arr = [a * b for a, b in zip(left, right)]

        print(result_arr)

        return result_arr
        