class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count_map = {}
        sorted_nums = sorted(nums)

        for index, value in enumerate(sorted_nums):
            if value not in count_map:
                count_map[value] = index

        ret = []
        for i in nums:
            ret.append(count_map[i])

        return ret

            
        
          
        


        
