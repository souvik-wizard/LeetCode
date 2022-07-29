# Not O(1) space but mine solution :)
def majorityElement(nums):
        if len(nums)==1:
            return nums
        hash={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]].append(i)
            else:
                hash[nums[i]]=[i]
        for key, values in hash.items():
            if len(nums)//3 < len(values):
                res.append(key)
        return res


# Another easy but O(1) space solution (learned)
from typing import Counter
def majorityElement(nums):
    l = len(nums)

    #Counter() --- is Kind of a hash map you can say
    c = Counter(nums)  

    # Using list comprehension
    return [i for i,j in c.items() if l//3 < j]




if __name__=="__main__":
    nums=[7,8,7,8]
    print (majorityElement(nums))