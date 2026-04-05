class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force takes O(n^2)

        hashSet = set(nums)
        print(hashSet)
        listOfSeq = dict()
        
        for num in nums:
            if num - 1 not in hashSet: # condition for new sequence
                new_seq = []
                new_seq.append(num)
                listOfSeq[num] = new_seq
            # else not a start of sequence so we dont do anything
        
        # print(listOfSeq)

        value = 1
        for key in listOfSeq:
            while key + value in hashSet: # iterate until no longer consecutive
                listOfSeq[key].append(key+value)
                value += 1
            value = 1

        print(listOfSeq)

        max_arr_len = 0
        for key in listOfSeq:
            if len(listOfSeq[key]) > max_arr_len:
                max_arr_len = len(listOfSeq[key])
        
        print(max_arr_len)

        return max_arr_len