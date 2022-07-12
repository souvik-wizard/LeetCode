# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        if n==1:
            return 1
        while low <=high:
            mid=(low+high)//2
            if guess(mid)==0:      
                return mid
            elif guess(mid)==-1:  #-1: Your guess is higher than the number I picked (i.e. num > pick)
                high=mid-1
                 
            else:
                low=mid+1   #1: Your guess is lower than the number I picked (i.e. num < pick)
                