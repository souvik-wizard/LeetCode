def repeatedCharacter(self, s: str) -> str:
    dict={}
    for i in range (len(s)):
        if s[i] in dict:
            return s[i]
        dict[s[i]]=[i]