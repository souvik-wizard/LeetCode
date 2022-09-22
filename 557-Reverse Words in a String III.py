class Solution:
    def reverseWords(self, s: str) -> str:
        s= s[::-1]
        s=s.split()
        l=len(s)-1
        for i in range(len(s)//2):
            temp=s[i]
            s[i]=s[l]
            s[l]=temp     
            l-=1          
        return " ".join(s)