# My solution

def pal(s):
    if s==" ":
        return True

    #  ''.join will join where it finds any space in the given string
    #  .isalnum() is Checking if all the characters in the text are alphanumeric(alphabets & numbers)
    s=''.join(i for i in s if i.isalnum())

    # converting the string to lowercase characters
    s=s.lower()
    start=0
    end=len(s)-1
    while start <= end:
        pass
        if s[start]==s[end]:
            start+=1
            end-=1
        else:return False
    return True



# Some learned but very useful solutions

# using filter
def isPalindrome(self, s: str) -> bool:
    s=''.join(filter(str.isalnum, s.lower()))
    return s==s[::-1]


# Using regular expression 
def isPalindrome(self, s: str) -> bool:
    s = re.sub('[^a-zA-Z0-9\n]', ' ', s)
    s = s.replace(' ', '').lower()
    return True if s == s[::-1] else False






if __name__=='__main__':
    s= "A man, a plan, a canal: Panama"
    print(pal(s))
