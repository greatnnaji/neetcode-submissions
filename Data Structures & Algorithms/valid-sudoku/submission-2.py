class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # for each row
        for row in board:
            newSet = set()
            for value in row:
                if value != ".":
                    if value not in newSet:
                        newSet.add(value)
                    else:
                        print("False: Contains duplicate: row wise")
                        return False
            print(newSet)
        
        # for each column
        index_rows = 0
        index_cols = 0
        while index_cols < 9:
            newSet = set()
            while index_rows < 9:
                current_val = board[index_rows][index_cols]
                if current_val != ".":
                    if current_val not in newSet:
                        newSet.add(current_val)
                    else:
                        print("False: Contains duplicate: column wise")
                        return False
                index_rows += 1
            index_rows = 0
            index_cols += 1
            # print(newSet)

        # for each 3x3
        col_reset = 3
        row_reset = 3

        index_y = 0

        index_y_move = 0
        index_x_move = 0

        update = 3

        while index_y < 9:
            newSetThree = set()
            if row_reset > 9:
                # print("reset")
                row_reset = 3
                col_reset += 3
                index_y += 3
                index_x_move = 0
                index_y_move = index_y
                # print(col_reset)
            while index_x_move < row_reset:
                while index_y_move < col_reset and col_reset <= 9:
                    # print(index_x_move, index_y_move)
                    current_value = board[index_x_move][index_y_move]
                    if current_value != ".":
                        if current_value not in newSetThree:
                            newSetThree.add(current_value)
                        else:
                            print("False: Contains duplicate: 3x3 wise")
                            return False
                    index_y_move += 1
                index_x_move += 1
                index_y_move = index_y
            # print(newSetThree)
            row_reset += update


        return True