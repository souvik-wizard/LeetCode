# Solution 1
class Solution:
    def hammingWeight(self, n: int) -> int:    
        n=str(bin(n))
        count=0
        for i  in n:
            if i=="1":
                count+=1
        return count

# Solution 2
def hammingWeight(self, n: int) -> int: 
    return bin(n).count("1")