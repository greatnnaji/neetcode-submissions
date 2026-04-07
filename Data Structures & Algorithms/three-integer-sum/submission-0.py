class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_arr = []
        nums = sorted(nums)
        left = 1
        right = len(nums) - 1

        start = 0
        while start < len(nums) - 2:
            while left < right:
                if nums[start] + nums[left] + nums[right] == 0:
                    new_trip = (nums[start], nums[left], nums[right])
                    triplet_arr.append(new_trip)
                    left += 1
                elif nums[start] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
            start += 1
            left = start + 1
            right = len(nums) - 1

        triplet_arr = list(set(triplet_arr))

        return triplet_arr