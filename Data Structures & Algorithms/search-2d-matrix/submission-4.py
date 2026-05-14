class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_total = len(matrix) * len(matrix[0])

        l = 0
        r = matrix_total - 1

        while l <= r:
            mid = r - l + 1//2
            print(mid)

            col = mid//len(matrix[0])
            row = mid % len(matrix[0]) 

            if matrix[col][row] == target:
                return True
            elif matrix[col][row] < target:
                l = mid + 1
            else:
                r = mid - 1
            

        return False