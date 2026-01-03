from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)
        for s in strs:
            mp[tuple(sorted(s))].append(s)
        return mp.values()
