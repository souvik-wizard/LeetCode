class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=sum(int(i) for i in (str(num)))
        return num


# Recursive Solution
class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        k=0
        for i in str(num):
            k+=int(i)
        return self.addDigits(k)