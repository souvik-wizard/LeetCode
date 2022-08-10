#Sol 1
# Using hash dict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_dict={}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                return True
            hash_dict[nums[i]]=[i]
        return False

# Sol 2
# Set concept can be use here as duplicate values can't be store in a set.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!= len(set(nums))