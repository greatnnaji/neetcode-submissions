class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        itera = 0

        while start < end:
            print("start: ", start)
            print("end: ", end)
            mid = (end - start)//2 + start
            print("Mid: ", mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                print("start + 1")
                start = mid + 1
            else: # nums[mid] > target
                print("end - 1")
                end = mid - 1
        
        print(start)
        print(end)
        if nums[start] == target: # start == end
            return start
        
        return -1
