# Best solution

#Set cannot contains same elements , it can store only one of them. 
#So if we sum set elements and then multiply them with 2 we get twice sum of all elements **Including the single one**
#Then we simply subtract it with the sum of all numbers in our given array.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)




# Another Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=nums[0]
        for i in range(1,len(nums)):
            res = res^nums[i]
        return res
        