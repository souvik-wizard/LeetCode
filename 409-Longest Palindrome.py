
# def longestPalindrome(self, s: str) -> int:
#         if len(s)==1:
#             return 1
#         hash_dict={}
#         out=0
#         for i in s:
#                 if s[i] not in hash_dict:
#                     hash_dict[s[i]] = [i]
#                 else:
#                     hash_dict[s[i]].append(i)
#         for key,values in hash_dict.items():
#             if len(values)%2 == 0:
#                 out+=len(values)
#             out+=1
#         return out
        





from typing import Counter


def pal(s):

    # Counter is similar to hash table value(number of times an item seen in str) and keys (the items itself) are there.
    c=Counter(s)
    print(c)
    out=0
    for i in c.values():
        print(i)
        out += int(i/2) * 2
        # print (out)
        if out % 2 == 0 and i%2==1:
            out+=1
    return out
        # print (i)





# def pal(s):
#         l = []
#         counter = 0
#         flag = False
#         for i in range(len(s)):
#             l.append(s[i])
#         p = collections.Counter(l)
#         for j,k in p.items():
#             if k%2 != 0:
#                 flag = True
#                 counter += k-1
#             if k%2 == 0:
#                 counter += k
#         if flag == True:
#             counter +=1 
#         return counter








if __name__=="__main__":
    s="abccccdd"
    print(pal(s))