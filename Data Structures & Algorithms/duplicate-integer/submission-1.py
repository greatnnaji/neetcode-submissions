class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums) #O(n)
        if(len(myset) < len(nums)):
            return True
        return False