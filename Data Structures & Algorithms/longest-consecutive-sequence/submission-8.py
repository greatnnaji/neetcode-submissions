class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        starts = []
        lcs = 0

        # find all unique start points
        for num in nums:
            if num - 1 not in numSet:
                starts.append(num)

        for s in starts:
            nxt = s + 1
            while nxt in numSet:
                nxt += 1
            
            lcs = max(lcs, nxt - s)

        return lcs
        

