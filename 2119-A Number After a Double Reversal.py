class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True      
        else:
            num=str(num)
            if len(num[::-1])==len(num.strip("0")):
                return True
            else:return False
