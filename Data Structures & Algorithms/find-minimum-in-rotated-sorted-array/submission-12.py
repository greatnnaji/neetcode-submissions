class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if nums[l] <= nums[mid]:
                # know for sure this is smallest on left half
                minVal = min(nums[l], minVal)
                l = mid + 1
            else:
                minVal = min(nums[mid], minVal)
                r = mid - 1
        
        return minVal
