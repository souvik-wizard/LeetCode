class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[pointer]:
                pointer+=1
                nums[pointer]=nums[i]
                # print(nums[pointer])
        return pointer+1
        
            