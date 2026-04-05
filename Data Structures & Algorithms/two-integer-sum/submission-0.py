class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_indices = []
        for i in range(len(nums)):            
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    target_indices.insert(0, i)
                    target_indices.insert(1, j)
                    break

        return target_indices

solution = Solution()
print(solution.twoSum([4,5], 9))