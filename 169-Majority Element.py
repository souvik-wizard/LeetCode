class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid=(len(nums)-1)//2
        return nums[mid]