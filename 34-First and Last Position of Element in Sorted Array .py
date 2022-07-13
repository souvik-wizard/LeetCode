#Solution 1 [using binary search]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binarySearch(nums,target,True)
        right=self.binarySearch(nums,target,False)
        return [left,right]
        
    def binarySearch(self,nums,target,leftBias): 
        low,high=0, len(nums)-1
        res=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                res=mid
                if leftBias:
                    high=mid-1
                else:
                    low=mid+1
        return res
                    


#Solution 2 [Using bisect method] --I personally liked it


import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left,right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
                
        return [left, right - 1] if left < right else [-1, -1]
    