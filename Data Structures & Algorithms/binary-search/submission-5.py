class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = len(nums)//2    
        left = 0
        right = len(nums) - 1

        while left < right:
            print("i: ", index)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                print(nums[index])
                print("greater")
                right = index - 1
                index = (right + left)//2
                print("idx_upd: ", index)
            elif nums[index] < target:
                print(nums[index])
                print("lesser")
                left = index + 1
                print("left: ", left)
                index = (right + left)//2
                print("idx_upd:" ,index)

        if nums[left] == target: return index

        return -1