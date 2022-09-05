class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True      
        else:
            num=str(num)
            #String strip() Method will remove the character from string
            #[rstrip() will remove from right & lstrip() will remove from left]
            if len(num[::-1])==len(num.strip("0")):
                return True
            else:return False
