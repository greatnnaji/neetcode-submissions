import heapq # by default a minheap

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points: # n log k
            heapq.heappush(heap, (-(x**2 + y**2), x, y)) # dont understand why this must be negative
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _, x,y in heap:
            res.append([x,y])

        return res
            