class Solution(object):
    def sortedSquares(self, nums):
        squares = []

        for num in nums:
            squares.append(num * num)

        return sorted(squares)
