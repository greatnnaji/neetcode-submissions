class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set(nums)
        if len(newSet) != len(nums):
            return True
        
        return False