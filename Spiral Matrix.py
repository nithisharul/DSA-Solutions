class Solution(object):
    def spiralOrder(self, matrix):
        ret = []
        while matrix:
            # 1) top row
            ret += matrix.pop(0)

            # 2) right column
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # 3) bottom row (reversed)
            if matrix:
                ret += matrix.pop()[::-1]

            # 4) left column (bottom → top)
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))

        return ret
