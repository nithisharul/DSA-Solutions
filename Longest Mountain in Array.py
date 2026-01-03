class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        ans = 0

        for i in range(1, n-1):
            # check if i is a peak
            if arr[i-1] < arr[i] > arr[i+1]:
                l = i
                r = i

                # expand left
                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1

                # expand right
                while r < n-1 and arr[r] > arr[r+1]:
                    r += 1

                ans = max(ans, r - l + 1)

        return ans


            
        return ret 
            

        
