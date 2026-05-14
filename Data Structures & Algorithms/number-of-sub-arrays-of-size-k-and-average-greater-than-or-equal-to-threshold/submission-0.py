class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # fixed size window

        sub_size = 0
        window_count = arr[:k]
        l = 0

        if k > len(arr):
            return 0

        avg = sum(window_count)/ len(window_count)
        if avg >= threshold:
            sub_size += 1

        for r in range(k , len(arr)):
            window_count.append(arr[r])
            window_count.remove(arr[l])
            l += 1

            # Check again
            avg = sum(window_count)/ len(window_count)
            if avg >= threshold:
                sub_size += 1
        
        return sub_size



