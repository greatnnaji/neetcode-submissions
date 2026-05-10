class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if nums[l] <= nums[mid]:
                minVal = min(minVal, nums[l])
                l = mid + 1
            else:
                minVal = min(minVal, nums[mid])
                r = mid - 1
            
        
            print(minVal)

        return minVal