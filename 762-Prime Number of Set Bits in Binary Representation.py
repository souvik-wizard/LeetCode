# O(n^2) solution
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:      
        arr=[]
        for k in range(left,right+1):
            arr.append(bin(k).count('1'))     
        prime=0
        for i in arr:   
            c=0
            for j in range(1,i):   
                if i%j == 0:
                    c+=1
            if c==1:
                prime+=1
        return prime