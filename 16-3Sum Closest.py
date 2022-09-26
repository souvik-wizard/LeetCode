# Sol 1
import sys
class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		n = len(nums)
		ans = 0
		diff = sys.maxsize

		for i in range(n):
			l , r = i + 1, n - 1

			while l < r:
				currSum = nums[i] + nums[l] + nums[r]

				if currSum == target:
					return currSum

				if currSum > target:
					r -= 1
				else:
					l += 1

				if abs(target - currSum) < diff:
					ans = currSum
					diff = abs(target - currSum)
		return ans

# Sol 2

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else: 
                    return res
        return res

# Sol 3

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        diff = 10000
        for cur_ind in range (len (nums)-1):
            left, right = cur_ind + 1, len(nums)-1 
            while left < right :
                threesum = nums[cur_ind] + nums[left] + nums[right]
                if threesum == target :
                    return threesum
                if abs(threesum - target) < diff:
                    diff = abs(threesum - target)
                    ans = threesum
                if threesum < target :
                    left += 1
                elif threesum > target:
                    right -= 1
        return ans