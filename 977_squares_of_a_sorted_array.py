class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in range(len(nums)):
            nums[x]=nums[x]**2     
        nums.sort()
        return nums
