# sol 1
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch=set(chars)
        res=0
        for i in words:
            if set(i).issubset(ch):
                arr=[j for j in set(i) if chars.count(j)<i.count(j)]       
                if len(arr)==0:
                    res+=len(i)
        return res

# sol 2
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        res = 0
        for w in words:
            msw = Counter(w)
            if msw & chars == msw:
                res += len(w)
        return res