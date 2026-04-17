class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [item for sublist in matrix for item in sublist]
        print(flat)

        start = 0
        end = len(flat) - 1

        while start <= end:
            mid = (end - start)//2 + start
            if flat[mid] == target:
                return True
            elif flat[mid] < target:
                start = mid + 1
            else: # flat[mid] > target:
                end = mid - 1
        
        return False







        return False