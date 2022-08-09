class Solution:
    def reverseBits(self, n: int) -> int:
            n  = bin(n)
            rev = n[-1:1:-1]
            x = rev + (32 - len(rev))*'0'
            return int(x,2)