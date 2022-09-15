class Solution:
    def rearrangeCharacters(self, s: str, t: str) -> int:
        d={}
        for i in t:
            if i not in d:
                d[i]=t.count(i)
        
        d1={}
        for i in t:
            if i not in d1:
                d1[i]=s.count(i)
        l=[]
        for i in d1:
            l.append(d1[i]//d[i])
        
        return min(l)

# linear sol
class Solution:
    def rearrangeCharacters(self, s: str, t: str) -> int:
        return min([Counter(s)[ch] // Counter(t)[ch] for ch in t])