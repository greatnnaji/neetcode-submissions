class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        
        for i, n in enumerate(nums):
            val = target - n
            if val in indices:
                return [indices[val], i]
            indices[n] = i
            
        return []