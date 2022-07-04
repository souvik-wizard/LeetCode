
def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for item in range(length//2):
            s[item], s[length-1-item] = s[length-1-item], s[item]



# OR


def reverseString(self, s: List[str]) -> None:
       s.reverse()