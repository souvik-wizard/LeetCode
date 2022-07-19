# A bit difficult to understand maybe

import math
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # nums1=nums1+nums2        #Time complexity O(n logn)
    nums1.extend(nums2)        #Time complexity O(n)
    nums1.sort()
    length=len(nums1)       
    if (length%2)==0:
        low=0
        high=length-1
        while low<=high:
            low+=1
            high-=1
        return (nums1[low]+nums1[high])/2
    else:
        mid=math.ceil(length//2)
        return nums1[mid]







# Simple approach

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()
    length = len(nums1)
    mid1 = length // 2
    if length % 2 == 1:
        return nums1[mid1]
    else:
        mid2 = (length // 2) - 1
        return (nums1[mid1] + nums1[mid2])/2