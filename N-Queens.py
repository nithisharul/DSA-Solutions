class Solution:
    def solveNQueens(self, n):
        res = []
        cols, d1, d2 = set(), set(), set()

        def dfs(r, board):
            if r == n:
                res.append(board[:])
                return
            for c in range(n):
                if c in cols or r-c in d1 or r+c in d2:
                    continue
                cols.add(c); d1.add(r-c); d2.add(r+c)
                dfs(r+1, board + ["."*c + "Q" + "."*(n-c-1)])
                cols.remove(c); d1.remove(r-c); d2.remove(r+c)

        dfs(0, [])
        return res
