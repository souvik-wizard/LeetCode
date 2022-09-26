# Combination() method takes a list and an input r as an input and return an object list of tuples.
# Which contain all possible combination of length r in a list form. 

# Combinations(nums,r) --> Here 'r' means all posssible r number of combinations . And nums is the list.

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        for a,b,c,d in combinations(nums,4):
            if a+b+c==d: ans +=1
        return ans