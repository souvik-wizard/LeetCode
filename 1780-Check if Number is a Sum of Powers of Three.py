class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
            while n > 0:
                if n % 3 == 2:
                    return False
                n = n // 3
            return True


# Sol 2
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            n, rem = divmod(n, 3)
            if rem == 2:
                return False
        return True