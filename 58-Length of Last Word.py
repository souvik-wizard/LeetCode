class Solution(object):
    def lengthOfLastWord(self, s):
        A=s.strip()
        B=A.split(" ")
        return len(B[-1])