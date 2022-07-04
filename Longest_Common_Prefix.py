
def prefix(strs):
    string=""
    index=0
    if len(strs)==0:
        return ""
    min_str_len=len(min(strs))
    while index < min_str_len:
        for item in strs:
            if item[index]!=item[index]:
                return string
        string+=strs[0][index]
        index+=1
    return string


print(prefix(["flower","flow","flight"]))


