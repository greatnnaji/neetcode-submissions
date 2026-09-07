class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        lcs = 0

        for num in nums:
            if num - 1 not in numSet:
                nxt = num + 1
                while nxt in numSet:
                    nxt += 1
        
                lcs = max(lcs, nxt - num)

        return lcs
        

