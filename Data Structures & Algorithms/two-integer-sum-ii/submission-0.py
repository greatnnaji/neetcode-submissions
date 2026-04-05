class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashMap = dict()

        for index,num in enumerate(numbers):
            hashMap[num] = index + 1

        print(hashMap)

        for index,num in enumerate(numbers):
            diff = target - num
            if diff in hashMap:
                if hashMap[diff] != index:
                    print(index)
                    print(hashMap[diff])
                    return [index + 1, hashMap[diff]]

        return []