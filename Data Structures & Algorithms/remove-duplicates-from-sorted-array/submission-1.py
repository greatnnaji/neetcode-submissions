class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for r, num in enumerate(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        
        return l + 1
