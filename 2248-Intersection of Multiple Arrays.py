class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1: return sorted(nums[0])
        res = [value for value in nums[0] if value in nums[1]]
        for i in range(1,len(nums)):
            res = [value for value in res if value in nums[i]]
        return sorted(res)