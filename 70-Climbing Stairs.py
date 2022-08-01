# Fibonacci Solution can be applied here (O(n)) .
class Solution:
    def climbStairs(self, n: int) -> int:
        s1=0
        s2=1
        for i in range (n):
            s1 , s2 = s2, s2+s1
        return s2

