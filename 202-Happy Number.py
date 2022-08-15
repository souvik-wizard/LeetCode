class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n not in s:
            s.add(n)
            n=sum(int(i)**2 for i in str(n))
            if n==1:
                return True            
        return False


# Recursive Solution
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n==7: return True
        if len(str(n)) < 2: return False

        st = sum(int(s)**2 for s in str(n)) 
        if st == 1: return True
        return self.isHappy(st)
