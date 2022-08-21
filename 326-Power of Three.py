# recursive method
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
            if (n <= 0):
                return False
            if (n == 1):
                return True
            if (n % 3 == 0):
                return self.isPowerOfThree(n // 3)



# Another logical method
'''The logic is very simple. Any integer number other than power of 3 which divides highest power of 3 value that integer can hold 3^19 = 1162261467 (Assuming that integers are stored using 32 bits) will give reminder non-zero.'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
            if n <= 0:return False
            """ The maximum power of 3 value that
       integer can hold is 1162261467 ( 3^19 ) ."""
            return 1162261467 % n == 0