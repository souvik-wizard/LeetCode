
def twoOutOfThree(self, num1: List[int], num2: List[int], num3: List[int]) -> List[int]:
        
        final=[]
        for i in range (len(num1)):
            if  num1[i] in num2:
                final.append(num1[i])
        for i in range (len(num2)):
            if  num2[i] in num3:
                final.append(num2[i])
        for i in range (len(num3)):
            if  num3[i] in num1:
                final.append(num3[i])
        return set(final)