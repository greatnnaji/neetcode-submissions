class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = []
        left_arr.append(1)
        index_l = 0
        while index_l < len(nums) - 1:
            left_arr.append(left_arr[-1] * nums[index_l])
            index_l += 1
        
        print(left_arr)

        right_arr = []
        right_arr.append(1)
        index_r = len(nums) - 1
        while index_r > 0:
            right_arr.insert(0, right_arr[0] * nums[index_r])
            index_r -= 1

        print(right_arr)

        prod_arr = []
        i = 0
        while i < len(nums):
            prod_arr.append(left_arr[i] * right_arr[i])
            i += 1

        print(prod_arr)

        return prod_arr
        