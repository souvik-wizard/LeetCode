# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n        
        if n==1:
            return 1       
        while low<=high:
            mid=(high+low)//2
            if isBadVersion(mid)==True:
                if isBadVersion(mid-1)==False:
                    return mid
                else:
                    high=mid-1           
            else:
                low=mid+1
        return -1
  