class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = len(nums)//2    
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[index] == target:
                return index
            elif nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            
            index = (right + left)//2

        if nums[left] == target: return index # left = right = index

        return -1