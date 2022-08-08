class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


# Another Approach learned [USING ASCII VALUE]

class Solution:
    def toLowerCase(self, s: str) -> str:
            d = ''
            for i in s:
                if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                    # Why 32?
                    # If we ADD 65+32 we get the small value for Capital A (Check ascii table for more info)
                    d += chr(ord(i) + 32)
                else:
                    d += i
            return d  


#OR
class Solution:
    def toLowerCase(self, s: str) -> str:
        ch = ""
        for i in s:
            # ord() use to get the ascii value in python
            asc = ord(i)
            # Capital letters in ascii table starts from 64-90
            # Small letters in ascii table starts from 97-122
            if asc > 64 and asc < 91:
                ch += chr(asc+32)
            else:
                ch +=chr(asc)
        return ch