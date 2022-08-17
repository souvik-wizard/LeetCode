class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]]=1
            else:
                dict[s[i]]+=1                       
        for i in range(len(s)):
            if dict[s[i]]==1:return i
        return -1
                       