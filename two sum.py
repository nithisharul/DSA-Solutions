class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in hashmap:
                return [i,hashmap[diff]]
            else:
                hashmap[v] = i
            
        
        
        
