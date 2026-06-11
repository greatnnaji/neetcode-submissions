class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        r = [1]

        for i in range(0, len(nums) - 1):
            j = len(nums) - 1 - i
            l.append(l[-1] * nums[i])
            r.append(r[-1] * nums[j])
        
        r.reverse()

        res = []

        for i in range(0, len(nums)):
            res.append(l[i] * r[i])

        return res


