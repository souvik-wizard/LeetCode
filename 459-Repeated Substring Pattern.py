# Sol 1
# Time complexity O(n sqrt(n))

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
                N = len(s)
                def pattern(n):
                    for i in range(0,N-n,n):
                        if s[i:i+n] != s[i+n:i+2*n]:
                            return False
                    return True
                for j in range(1,N // 2+1):
                    if pattern(j): return True
                return False

# Sol2

# This solution is quite tricky
# Because it somehow rotate the string and after that if any repeated substring exists 
# then it will return the same string excluding the first and last character.
# Thats why we used [1:] and [:-1] here to exclude the first and last cahracter
# This is a O(n) solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
                string=s[1:]+s[:-1]
                return s in string

# OR
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]  