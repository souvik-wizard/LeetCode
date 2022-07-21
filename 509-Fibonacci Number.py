# Using while loop

class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        start=0
        end=1
        s=start+end
        while (n>1):
            s=start+end
            start=end
            end=s
            n-=1
        return s

# Using recursion 


class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)