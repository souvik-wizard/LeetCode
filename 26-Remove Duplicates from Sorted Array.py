class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[pointer]:
                pointer+=1
                nums[pointer]=nums[i]
                # print(nums[pointer])
        # print(pointer)
        return pointer+1
        
            
# easy to understand solution
class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        while k < len(nums): 
            if nums[k - 1] == nums[k]:
                nums.pop(k)
            else:
                k += 1
        return k