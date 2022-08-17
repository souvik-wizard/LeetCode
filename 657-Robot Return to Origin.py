class Solution:
    def judgeCircle(self, moves: str) -> bool:
        i,j=0,0
        for m in moves:
            if m=='U':
                i+=1
            if m=='D':
                i-=1
            if m=='L':
                j-=1
            if m=='R':
                j+=1
        return i==0 and j==0