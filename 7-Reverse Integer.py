# My solution
class Solution:
    def reverse(self, x: int) -> int:
        checking=1
        if x<0:
            checking=-1
        x=abs(x)
        rev=int(str(x)[::-1])
        if -2147483648<rev*checking<2147483648:
            return rev*checking
        else:return 0

# Explanation !
# initally we set our checking to positive
# then we check whether our number is neg or not
# if yes we'll make "checking"=negative   Why so?  -->to make our final result negative if a negative input is given
# we set our given number to positive number by using abs()
# then We need to first stringify our input, then use slicing method to reverse the string ( x[start:stop:step] )
# after that again convert that reversed string to integer  and storing it in "rev"

# Here is the interesting part 
# The reversed integer must stands between[-2^31 , 2^31 - 1] (bcz of 32 bit)
# The maximum and minimum 32 bit number is max(2147483648) and min(-2147483648)
#  [ You can write 2**31 and (-2**31)-1 instead of  2147483648 , -2147483648 ]
# if true then we multiply our reversed number 'rev' to 'checking' to make it positive or negative whatever given initially
# else we return 0 [If reversed integer is not between (-2^31 , 2^31 - 1) ]


# Another using while loop
class Solution:
    def reverse(self, x: int) -> int:
        checking=1
        if x<0:
            checking=-1
        x=abs(x)
        rev=0
        while(x > 0):
            temp = x % 10
            rev = rev * 10 + temp
            x = x // 10
        if -2147483648<rev*checking<2147483648:
            return rev*checking
        else:return 0

