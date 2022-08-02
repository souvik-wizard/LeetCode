# First  method  - I think I invented, NVM :)


class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(x**0.5)





# Alternative method


import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))


