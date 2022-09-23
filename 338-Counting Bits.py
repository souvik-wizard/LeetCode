class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]
        for i in range(n+1):
            arr.append (bin(i).count('1'))
        return arr

# One line code
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]