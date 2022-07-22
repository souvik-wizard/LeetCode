# Using cool method (Swapping elements)
class Solution:
    def fib(n):
        num1=0
        num2=1
        num3=1
        for i in range (n):
            num1 , num2 ,num3 = num2 , num3, num1+num2 + num3
        return num1


    if __name__=='__main__':
        print(fib(25))