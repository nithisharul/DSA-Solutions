class Solution:
    def solveSudoku(self, board):
        # bitmask for rows, cols, boxes
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        # initialize bitmasks
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    num = int(board[i][j]) - 1
                    mask = 1 << num
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i//3)*3 + j//3] |= mask

        def dfs(pos=0):
            if pos == len(empties):
                return True
            i, j = empties[pos]
            b = (i//3)*3 + j//3
            # bitmask of used numbers
            used = rows[i] | cols[j] | boxes[b]
            for num in range(9):
                mask = 1 << num
                if not (used & mask):
                    # place number
                    board[i][j] = str(num + 1)
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[b] |= mask

                    if dfs(pos + 1):
                        return True

                    # backtrack
                    board[i][j] = '.'
                    rows[i] &= ~mask
                    cols[j] &= ~mask
                    boxes[b] &= ~mask
            return False

        dfs()
