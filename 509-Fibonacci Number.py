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



# Using Swapping (Cool one) 

class Solution:
    def fib(self, n: int) -> int:
        num1=0
        num2=1
        for i in range (n):
            num1 , num2 = num2 , num1 + num2
        return num1
