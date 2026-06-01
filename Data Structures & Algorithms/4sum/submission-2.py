class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        quad = set()
        a = 0
        n = len(nums)

        for a in range(n):
            for b in range(a + 1, n):
                c = b + 1
                d = n - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    if total == target:
                        quad.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
                    elif total < target:
                        c += 1
                    else:
                        d -= 1

        return list(quad)



