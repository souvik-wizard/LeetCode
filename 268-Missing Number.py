# 166ms
def missingNumber(nums):
        n= len(nums)
        prev_sum = n*(n+1)//2
        
        new_sum = sum(nums)
        
        return prev_sum - new_sum

print(missingNumber([0,1,3]))



# 297ms
def array(num):
    if len(num)==1 and num[0]==0:
        return 1
    if len(num)==1:
        return 0
    num.sort()
    length=len(num)
    for i in range(length):
        if i!=num[i]:
            return i
    return length

print(array([0,1,3]))
