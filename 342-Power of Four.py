# recursive method
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
            if (n <= 0):
                return False
            if (n == 1):
                return True
            if (n % 4 == 0):
                return self.isPowerOfFour(n // 4)

# using log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
            return n > 0 and log(n,4)%1 == 0