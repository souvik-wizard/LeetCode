# Efficient Solution
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int: 
        c=0
        s = str(num)
        for i in range(len(s)-k+1):
            t = int(s[i:k+i])
            if t!=0 and num%t==0:
                c+=1
        return c

# First in mind
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num=str(num)
        res=0
        if len(num)==1:
            if int(num)%k==0:
                res+=1
        else:
            for i in range(len(num)-k+1):
                if int(num[i:i+k])!= 0 and int(num) % int(num[i:i+k])==0:
                    res+=1
        return res

