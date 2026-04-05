class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
    
        # find and store start points
        numList = []
        for num in nums:
            if num - 1 not in nums_set:
                numList.append([num])
        
        # populate list
        for num_arr in numList:
            while num_arr[-1] + 1 in nums_set:
                num_arr.append(num_arr[-1] + 1)
        
        # get max length
        max_len = 0
        for arr in numList:
            if len(arr) > max_len:
                max_len = len(arr)
        
        return max_len
        
        
