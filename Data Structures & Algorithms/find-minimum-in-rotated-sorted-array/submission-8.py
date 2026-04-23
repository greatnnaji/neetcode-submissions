class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = 1000

        while l <= r:
            mid = (l + r)//2

            if nums[mid] >= nums[l]:
                # search right
                minVal = min(nums[l], minVal)
                l = mid + 1
            else:
                # search left
                minVal = min(nums[mid], minVal)
                r = mid - 1
            
        return minVal
