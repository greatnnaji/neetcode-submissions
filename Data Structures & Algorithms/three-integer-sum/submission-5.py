class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        sorted_nums = sorted(nums)

        arr_list = []

        newSet = set()

        print(sorted_nums)

        right = len(nums) - 1
        for i,nums_i in enumerate(sorted_nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                print(sorted_nums[i], sorted_nums[left], sorted_nums[right])
                if sorted_nums[i] + sorted_nums[left] + sorted_nums[right] > 0:
                    print("greater than zero")
                    right -= 1
                elif sorted_nums[i] + sorted_nums[left] + sorted_nums[right] < 0:
                    print("less than zero")
                    left += 1
                else:
                    print("triplet found...")
                    # num_sort = sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    newString = str(sorted_nums[i]) + str(sorted_nums[left]) + str(sorted_nums[right])
                    # print(newString)
                    # print(sorted_nums[i], sorted_nums[left], sorted_nums[right])
                    if newString not in newSet:
                        newSet.add(newString)
                        arr_list.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1

        
        # print(arr_list)
        return arr_list
        



                

        