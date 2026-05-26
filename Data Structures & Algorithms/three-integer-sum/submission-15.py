class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        trip_list = set()

        l = 0
        r = len(nums) - 1

        while l+1 < r:
            t = l + 1
            r = len(nums) - 1
            while t < r:
                if nums[l] + nums[t] + nums[r] == 0:
                    trip_list.add((nums[l], nums[t], nums[r]))
                    t += 1
                elif nums[l] + nums[t] + nums[r] < 0:
                    t += 1
                else:
                    r -= 1
            l += 1

        return list(trip_list)