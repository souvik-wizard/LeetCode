class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
                l1=len(nums1)
                l2=len(nums2)
                arr=[]
                if l1>l2:
                    for i in range(l2):
                        if  nums2[i] in nums1:
                            arr.append(nums2[i])
                else:
                    for i in range (l1):
                        if nums1[i] in nums2:
                            arr.append(nums1[i])
                return set(arr)
                           