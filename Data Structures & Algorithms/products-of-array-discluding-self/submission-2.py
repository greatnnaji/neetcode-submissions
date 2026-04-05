class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create left and right list st. current index is the running product of values
        # to the left and right
        left = []
        right = []

        left.append(1)# nothing to the left of first value in an array
        index_left = 0
        while index_left < len(nums) - 1:
            left.append(left[-1] * nums[index_left])
            index_left += 1
        
        # print(left)

        right.append(1)
        index_right = len(nums) - 1
        while index_right > 0:
            right.insert(0, (nums[index_right] * right[0]))
            index_right -= 1

        # print(right)
        
        i = 0
        prod_array = []

        while i < len(nums):
            prod_array.append(left[i] * right[i])
            i += 1
        
        # print(prod_array)


        return prod_array
