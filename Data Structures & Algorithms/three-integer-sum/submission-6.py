class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array
        sorted_nums = sorted(nums)

        uniqueSet = set()

        print(sorted_nums)

        left = 0
        right = len(sorted_nums) - 1
        for index,num in enumerate(sorted_nums):
            left = index + 1
            while left < right:
                print("value at i,j,k: ", (sorted_nums[index],sorted_nums[left], sorted_nums[right]))
                if sorted_nums[index] + sorted_nums[left] + sorted_nums[right] > 0:
                    print("greater")
                    right -= 1
                elif sorted_nums[index] + sorted_nums[left] + sorted_nums[right] < 0:
                    print("lesser")
                    left += 1
                else: 
                    print("triple found")
                    newTuple = (sorted_nums[index], sorted_nums[left], sorted_nums[right])
                    uniqueSet.add(newTuple)
                    left += 1 # next iteration

            right = len(sorted_nums) - 1

        arr_list = []
        for tuples in uniqueSet:
            newList = list(tuples)
            arr_list.append(newList)
    
        # print(uniqueSet)
        print(arr_list)

        return arr_list
        