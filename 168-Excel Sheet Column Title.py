class Solution(object):
    def convertToTitle(self, columnNumber):
        output = ""
        while columnNumber > 0:
            # Subtract 1 from columnNumber and get current character by doing modulo of columnNumber by 26
            output = chr(ord('A') + (columnNumber - 1) % 26) + output
            columnNumber = (columnNumber - 1) // 26
        return output



# Recursive Solution
# if number is less than "26", simply hash out (index-1)
# There are sub possibilities in possibilities,
# 1.if remainder is zero(if quotient is 1 or not 1) and
# 2. if remainder is not zero
class Solution(object):
    def convertToTitle(self, num):
            alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if num < 26:
                return alpha[num-1]
            else:
                q, r = num//26, num % 26
                if r == 0:
                    if q == 1:
                        return alpha[r-1]
                    else:
                        return self.convertToTitle(q-1) + alpha[r-1]
                else:
                    return self.convertToTitle(q) + alpha[r-1]