
def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1
        hash_dict={}
        out=0
        for i in s:
                if s[i] not in hash_dict:
                    hash_dict[s[i]] = [i]
                else:
                    hash_dict[s[i]].append(i)
        for key,values in hash_dict.items():
            if len(values)%2 == 0:
                out+=len(values)
            out+=1
        return out
        
                    
        