class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s={}
        hash_t={}      
        for sch,tch in zip(s,t):                       
            if (sch in hash_s and hash_s[sch]!=tch): 
                return False
            if (tch in hash_t and hash_t[tch]!=sch):
                return False     
            hash_s[sch]=tch
            hash_t[tch]=sch
        return True



 
#  Same but easy to undertand               
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        shash={}
        thash={} 
        for i in range(len(s)):
            sch=s[i]
            tch=t[i]
            if sch not  in shash:
                shash[sch]=tch
            if tch not in thash:
                thash[tch]=sch
            if shash[sch]!=tch or thash[tch]!=sch:
                return False
        return True




    if __name__=="__main__":
        s = "badc"
        t = "baba"
        print (isIsomorphic(s,t))