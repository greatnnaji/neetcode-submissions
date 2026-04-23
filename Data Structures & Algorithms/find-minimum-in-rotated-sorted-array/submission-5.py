class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = 1000

        while l <= r:
            mid = (l + r)//2

            if nums[mid] >= nums[l]: # remove equal to see purpose
                # search right
                if nums[l] < minVal:
                    minVal = nums[l]
                l = mid + 1
            else:
                # search left
                minVal = nums[mid]
                r = mid - 1
            
        print(minVal)

        # while l <= r:
        #     print("l: ", l)
        #     print("r: ", r)
        #     print("dist: ", abs(l - r))
        #     mid = (l + r)//2
        #     print("mid: ", mid)
        #     print("nums[mid]: ", nums[mid])
            
        #     if nums[mid] < minVal:
        #         minVal = nums[mid]
        #         r = mid - 1
        #         if r < 0:
        #             r = len(nums) - 1
        #     else:
        #         l = mid + 1
        #         if l == len(nums):
        #             l = 0
        #     # if t == 4:
        #     break
        #     # t += 1
        #     # print("L: ",l)
        #     # print("R: ", r)
        
        # # print(minVal)
        # # print("l:", l)
        # # print("r: ", r)

        # if nums[l] < minVal:
        #     return nums[l]

        return minVal
