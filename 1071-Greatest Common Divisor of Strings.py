from math import*
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
         return str1[:(str1+str2==str2+str1)*gcd(len(str1),len(str2))]