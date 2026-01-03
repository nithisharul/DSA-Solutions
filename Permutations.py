class Solution:
    def permute(self, nums):
        res = []
        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for n in nums:
                if n not in path:
                    path.append(n)
                    dfs(path)
                    path.pop()
        dfs([])
        return res
