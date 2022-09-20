class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        for i in nums1[:]:
            if i in nums2:
                nums1.remove(i)
                nums2.remove(i)
        return [nums1,nums2]


# 2 linear solutions
# 1) 
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
            return [set(nums1)-set(nums2), set(nums2)-set(nums1)]
# 2)
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
            return [[j for j in set(nums1) if j not in nums2],[i for i in set(nums2) if i not in nums1]]

