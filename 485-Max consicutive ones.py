def findMaxConsecutiveOnes(nums):
        max_one = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if count > max_one:
                max_one = count
        return max_one

print(findMaxConsecutiveOnes([1,1,0,1,1,1,1]))