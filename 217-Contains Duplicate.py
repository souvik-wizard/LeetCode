class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_dict={}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                return True
            hash_dict[nums[i]]=[i]
        return False