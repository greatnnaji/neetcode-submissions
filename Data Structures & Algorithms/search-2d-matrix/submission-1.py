class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        size = m * n
        print("m: ", m)
        print("n: ", n)
        print("size: ", size)

        # start = matrix[0][0]
        # endx = (size - 1)//n
        # endy = (size - 1) % n
        # end = matrix[endx][endy]

        start = 0
        end = size - 1

        while start <= end:
            mid_idx = (end - start)//2 + start
            midx = mid_idx//n
            midy = mid_idx % n
            mid = matrix[midx][midy]

            if mid == target:
                return True
            elif mid < target:
                start = mid_idx + 1
            else:
                end = mid_idx - 1

        return False