class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones_count = 0
        maxLen = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                ones_count += 1
            print("z: ", ones_count)

            if (r - l + 1) - ones_count > k:
                print("greater")
                if nums[l] == 1:
                    print("reducing zero..")
                    ones_count -= 1
                l += 1
                
            maxLen = max(maxLen, r - l + 1)
            print("maxLen: " ,maxLen)
            
            print("l: ", l)
            print("r: ", r)
        
        return maxLen
