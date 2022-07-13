class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if target==nums[mid]:
                result=mid
                return result
            elif target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return high+1
        