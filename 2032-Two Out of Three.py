# my solution
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        final=[]
        for i in range (len(nums1)):
            if  nums1[i] in nums2:
                final.append(nums1[i])
        for i in range (len(nums2)):
            if  nums2[i] in nums3:
                final.append(nums2[i])
        for i in range (len(nums3)):
            if  nums3[i] in nums1:
                final.append(nums3[i])
        return set(final)


# Some learned methods

# Concept of intersaction and union from mathematics
def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    set1,set2,set3 = set(nums1),set(nums2),set(nums3)
    
    a = list(set1.intersection(set2))
    b = list(set1.intersection(set3))
    c = list(set2.intersection(set3))
    
    
    return list(set(a+b+c))


# Concept of bitwise operators
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)