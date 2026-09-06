class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] # running prefix total
        r = [1] # running suffix total
        
        i = 0
        while i < len(nums) - 1:
            l.append(l[-1] * nums[i])
            i += 1
        
        j = len(nums) - 1
        while j > 0:
            r.append(r[-1] * nums[j])
            j -= 1
        
        res = []
        for i in range(len(nums)):
            res.append(l[i] * r[len(nums) - 1 - i])

        return res