class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] # what comes after curr idx
        r = [1] # what comes before curr idx
        length = len(nums)

        for i in range(length - 1):
            r.append(r[-1] * nums[i])
        
        for i in range(length - 1, 0, -1):
            l.append(l[-1] * nums[i])

        res = []
        for i in range(length):
            res.append(l[length - i - 1] * r[i])

        return res