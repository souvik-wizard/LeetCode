class Solution(object):
    def lengthOfLastWord(self, s):
        #strip will remove the space from start and end(if any)
        A=s.strip()
        B=A.split(" ")
        return len(B[-1])