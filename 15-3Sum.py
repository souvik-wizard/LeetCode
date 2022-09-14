# Solution 1 Easy and beginner friendly
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                nums.sort()
                res = []
                for i in range(len(nums)-1):
                    l = i + 1
                    r = len(nums) - 1
                    while l < r:
                        if nums[i] + nums[l] + nums[r] == 0:
                            res.append((nums[i], nums[l], nums[r]))
                            l += 1
                            r -= 1
                        elif nums[i] + nums[l] + nums[r] > 0:
                            r -= 1
                        else:
                            l += 1
                return set(res)



# optimal Solution 2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            res = []
            nums.sort()
            for i, j in enumerate(nums):
                if i>0 and j == nums[i - 1] :
                    continue
                l, r = i + 1, len(nums) - 1
                while l < r:
                    threeSum = j + nums[l] + nums[r]
                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0:
                        l += 1
                    else:
                        res.append([j, nums [l] , nums [r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
            return res
     
     

