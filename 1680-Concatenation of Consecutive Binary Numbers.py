class Solution:
    def concatenatedBinary(self, n: int) -> int:
        arr=[]
        for i in range(1,n+1):
            arr.append(bin(i)[2:])
        a=''.join(arr)
        return (int(a,2)%(10**9+7))

# Oneline Solution
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join([bin(i)[2:] for i in range(1,n+1)]),2) % (10**9+7)