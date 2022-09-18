# Similar as problem no. 2248

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words)==1:return list(words[0])
        s=Counter(words[0])
        for w in words:
            s &= Counter(w)
        #  .elements will take all the chs from s and print elements acording to its corrosponding values
        # As an example if [Counter({'l': 2, 'e': 1,'a': 5})] 
        # then it will print l 2times , e 1time and a 5times

        # i.e it will parse the Counter 
        return s.elements()