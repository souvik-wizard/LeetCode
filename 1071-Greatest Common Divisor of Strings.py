from math import*
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
         return str1[:(str1+str2==str2+str1)*gcd(len(str1),len(str2))]



# Easy to  understand sol
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 == str2:
            return str1

        if str1+str2 != str2+str1:
            return ""
        
        x = gcd(len(str1), len(str2))
        
        if str1[:x] == str2[:x]:
            return str1[:x]
        else:
            return ""