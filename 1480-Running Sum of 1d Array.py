class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        for i in range(n-1):
            nums[i+1] = nums[i]+nums[i+1]
        return nums