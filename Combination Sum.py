class Solution:
    def combinationSum(self, c, target):
        res = []
        def dfs(i, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target or i == len(c):
                return
            dfs(i, path+[c[i]], total+c[i])
            dfs(i+1, path, total)
        dfs(0, [], 0)
        return res
