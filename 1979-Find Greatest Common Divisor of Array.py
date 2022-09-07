# O(n) time O(1)space Efficient Sol
class Solution:
    def findGCD(self, nums: List[int]) -> int:
            mx=max(nums)
            mn=min(nums)
            res=1
            for i in range(1,mn+1):
                if  mx%i==0 and  mn%i==0:
                    res=i
            return res



# Brute force O(n)time and space
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn,mx=min(nums),max(nums)
        mn_div=[]
        mx_div=[]
        for i in range (1,mn+1):
            if mn%i==0:
                mn_div.append(i)
        for j in range (1,mx+1):
            if mx%j==0:
                mx_div.append(j)
        return max([x for x in mn_div if x in mx_div])