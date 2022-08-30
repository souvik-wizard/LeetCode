class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero,one,two = 0,0,0
        for i in range(len(nums)):
            if(nums[i] == 0): zero +=1
            elif(nums[i] == 1): one +=1
            elif(nums[i] == 2): two +=1
        s = "0"*zero + "1"*one + "2"*two
        # print(s) --> 001122
        for i in range(len(s)):
            nums[i] = s[i]