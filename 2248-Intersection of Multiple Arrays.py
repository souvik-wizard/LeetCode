# Similar problem as problem no. 1002
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1: return sorted(nums[0])
        res = [value for value in nums[0] if value in nums[1]]
        for i in range(1,len(nums)):
            res = [value for value in res if value in nums[i]]
        return sorted(res)


# solution 2
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        a = set(nums[0])
        for i in nums[1:]:
            # Same as & operation if both 1 then only output 1 
            # & is a bitwise operator and it  will take take only common values 
            a &= set(i)
        return sorted(a)
