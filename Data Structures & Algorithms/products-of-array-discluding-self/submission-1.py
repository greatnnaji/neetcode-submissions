class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make running product from left side and running product from right side
        left = []
        right = []

        left.append(1)
        for index, num in enumerate(nums):
            if index < len(nums)-1: # exclude last element
                left.append(left[-1] * nums[index])
        
        # print(left)

        right.append(1)
        for index in range(len(nums)-1, -1, -1):
            if index > 0: # exclude first element
                right.insert(0, right[0] * nums[index])
        
        # print(right)

        prod_arr = []

        index = 0
        while index < len(nums):
            prod_arr.append(left[index] * right[index])
            index += 1
        
        # print(prod_arr)

        return prod_arr