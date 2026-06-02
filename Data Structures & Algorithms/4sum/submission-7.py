class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quad = []
        nums.sort()
        n = len(nums)
        print(nums)

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            for b in range(i + 1, n):
                if b > i + 1 and nums[b] == nums[b - 1]:
                    continue
                    
                c = b + 1
                d = n - 1
                while c < d:
                    print(a,nums[b],nums[c],nums[d])
                    total = a + nums[b] + nums[c] + nums[d]

                    if total == target:
                        print("found")
                        quad.append([a, nums[b], nums[c], nums[d]])
                        c += 1
                        while nums[c] == nums[c - 1] and c < d:
                            c += 1
                    elif total < target:
                        print("lower")
                        c += 1
                    else:
                        print("higher")
                        d -= 1
                
                print(quad)

        return quad