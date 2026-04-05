class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create hashset for 0(1) lookup
        hashSet = set(nums)

        hashMap = dict()

        # find all starting sequences
        for num in nums:
            if num - 1 not in hashSet: # new sequence
                hashMap[num] = [num]
        
        # print(hashMap)

        # update sequences
        for numKey in hashMap:
            value = 1
            while numKey + value in hashSet:
                hashMap[numKey].append(numKey + value)
                value += 1
        
        # get largest list size
        maxSize = 0
        for numKey in hashMap:
            if len(hashMap[numKey]) > maxSize:
                maxSize = len(hashMap[numKey])

        # print(hashMap)

        # print(maxSize)

        return maxSize