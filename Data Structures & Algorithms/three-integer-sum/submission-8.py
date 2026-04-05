class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort: n log n
        sorted_nums = sorted(nums)

        print(sorted_nums)

        triplet_list = []

        left = 0
        right = len(nums) - 1

        for index, num in enumerate(sorted_nums):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                print("current_pair: ", (num, sorted_nums[left], sorted_nums[right]))
                if num + sorted_nums[left] + sorted_nums[right] == 0:
                    # store as tuples for acheiving uniqueness later
                    print("triplet found: ", (num, sorted_nums[left], sorted_nums[right]))
                    new_triplet = (num, sorted_nums[left], sorted_nums[right])
                    left += 1
                    triplet_list.append(new_triplet)
                elif num + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                elif num + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1

        print(list(set(triplet_list)))
        triplet_list = list(set(triplet_list))

        return triplet_list