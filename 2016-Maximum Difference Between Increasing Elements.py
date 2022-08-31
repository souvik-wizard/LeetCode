class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = nums[0]
        diff = 0
        for num in nums:
            diff = max(diff, num - mn) 
            print (diff)
            mn = min(mn, num)
        return diff or -1