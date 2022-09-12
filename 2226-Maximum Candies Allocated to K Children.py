class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:return 0
        else:
            low=0 
            high=max(candies)
            while low<high:
                mid=(low+high)//2+1
                if sum(c//mid for c in candies)>=k: low=mid
                else: high=mid-1
            return low

# Using biscet (one line sol)
class Solution:
    def maximumCandies(self, C: List[int], k: int) -> int:
        return bisect_left(range(1,sum(C)//k+1), True, key=lambda x:sum(c//x for c in C)<k)