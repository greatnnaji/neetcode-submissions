class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # assert that len nums > 2
        if len(nums) < 3:
            return []

        if len(nums) == 3: # len(nums) == 3 base case
            total_sum = 0
            for num in nums:
                total_sum += num
            
            if total_sum == 0:
                return [nums]

        else: # len(nums) > 3
            print("greater than 3")

            nums_hashMap = dict()

            # sorted_nums = sorted(nums)
            # print(sorted_nums)

            for index,num in enumerate(nums):
                nums_hashMap[num] = index
            
            print(nums_hashMap)

            arr_list = []

            set_array = set()

            for i, num_i in enumerate(nums):
                for j, num_j in enumerate(nums):
                    if i != j:
                        # print("i: ", i)
                        # print("nums[i]: ", num_i)
                        # print("j:", j)
                        # print("nums[j]: ", num_j)
                        target = -(nums[i] + nums[j])
                        # print("target: ", target)
                        if target in nums_hashMap:
                            if nums_hashMap[target] != i and nums_hashMap[target] != j:
                                print("triplet found...")
                                triplet = (nums[i], nums[j], target)
                                numeric_sort = sorted([nums[i], nums[j], target])
                                # print("numeric_sort: ", numeric_sort[0])
                                newString = str(numeric_sort[0]) + str(numeric_sort[1]) + str(numeric_sort[2])
                                if newString not in set_array:
                                    set_array.add(newString)
                                    arr_list.append(triplet)

                                # print(newString)
                                # print(newString)
                                # print(nums[i], nums[j], target)
                                # print(triplet)
                                # arr_list.append(triplet)
            return arr_list
                                

            print(arr_list)

        return []