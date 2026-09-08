class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = 0
        starts = []
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet: # num is a start
                nxt = num + 1
                while nxt in numSet:
                    nxt += 1
                lcs = max(lcs, nxt - num)
        
        return lcs