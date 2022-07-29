def isValid(s):
        if len(s)%2 != 0 :
            return False
        hash={ '(':')' , '{':'}', '[':']'}
        stack=[]
        for i in s:
            if i  in hash:                
                stack.append(i)
            else:
                if len(stack) == 0 or hash[stack.pop()] != i:
                    return False 
        if len(stack)>0:
            return False            
        return True



if __name__=="__main__":
    s="()][{}"
    print (isValid(s))