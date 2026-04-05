class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # iterate and check row wise
        newSetRow = set()
        duplicate_row = True

        for index,inner_arr in enumerate(board):
            for index,value in enumerate(board[index]):
                if value != ".":
                    if value not in newSetRow:
                        newSetRow.add(value)
                    else:
                        print("duplicate detected: row wise")
                        duplicate_row = False
                        return duplicate_row
            # next row
            # print(newSetRow)
            newSetRow = set()
        
        # print(duplicate_row)

        # iterate and check column wise
        newSetCol = set()
        duplicate_col = True

        i = 0 # index rows
        j = 0 # index cols
        while i < 9:
            j = 0
            while j < 9:
                # print(j, i)
                if board[j][i] != ".":
                    if board[j][i] not in newSetCol:
                        # print(board[j][i])
                        newSetCol.add(board[j][i])
                    else:
                        print("duplicate detected: column wise")
                        duplicate_col = False
                        return duplicate_col
                j += 1
            # next col
            # print(newSetCol)
            newSetCol = set()
            i += 1

        # print(duplicate_col)

        # iterate 3 x 3 grid wise        
        newSetLimit = set()
        duplicate_limit = True

        i = 0 # index rows
        j = 0 # index cols
        limit_i = i
        limit_j = j
        limit_j_max = 3
        limit_i_max = 3
        limit_i_start = 0

        while i < 9 and limit_i_max <= 9:
            # print("limit_j_max: ")
            # print(limit_j_max)
            # print("limit_j: ")
            # print(limit_j)
            
            if limit_j_max > 9: # reached end of a column
                # print("limit_i_start :")
                # print(limit_i_start)
                limit_i_start = limit_i
                # print("limit_i_max: ")
                # print(limit_i_max)
                limit_i_max += 3

            if i % 3 == 0:
                limit_j = 0
                limit_j_max = 3

            while limit_j < limit_j_max and limit_j_max <= 9:
                limit_i = limit_i_start
                while limit_i < limit_i_max:
                    if board[limit_j][limit_i] != ".":
                        if board[limit_j][limit_i] not in newSetLimit:
                            # print(board[limit_j][limit_i])
                            newSetLimit.add(board[limit_j][limit_i])
                        else:
                            print("duplicate detected: limit wise")
                            duplicate_limit = False
                            return duplicate_limit
                    limit_i += 1
                limit_j += 1

            print(newSetLimit)
            newSetLimit = set()
            # print(limit_j)
            limit_j_max += 3
            i += 1


        return True