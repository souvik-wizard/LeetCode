def square(array):
    a=[]
    for i  in range(len(array)):
        a.append( array[i]*array[i])
    return sorted(a)
        

if __name__=='__main__':
    array=[-3,-2,-1,0,2,4,6,8]
    print(square(array))