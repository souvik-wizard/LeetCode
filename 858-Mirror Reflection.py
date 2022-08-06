# Accepted Solution
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p==q:return 1
        while p%2==0 and q%2==0:
            p=p//2
            q=q//2
            
        if p%2==0 and q%2 !=0:return 2
        elif p%2 !=0 and q%2!=0: return 1
        elif p%2!=0 and q%2 ==0 : return 0





# Need to modify(not accepted)

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p==q:return 1
        i=math.log2(p)
        if q+q==p or i==int(i):return 2  
        if p%2==0:
            if q%2!=0: return 2
            if q%2==0: 
                if p%q==0: return 2 
            if q>p//2 and q%2==0: return 2
               
        else:
            if q%2 ==0:return 0
            elif p%2 !=0: return 1