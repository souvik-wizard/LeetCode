# Optimized appproach O(n)

def square(array):
    low=0
    high=len(array)-1
    a=[]
    while low<=high:
        if array[low]**2 > array[high]**2:
            a.append(array[low]**2)
            low+=1
        else:
            a.append(array[high]**2)
            high-=1
    return a[::-1]




# Some basic approach 1  #O(n logn)
def square(array):
    a=[]
    for i  in range(len(array)):
        a.append( array[i]**2)
    return sorted(a)  




# # Some basic approach 2
         
def square(array):
    return sorted([array**2 for array in array])





if __name__=='__main__':
    array=[-3,-2,-1,0,2,4,6,8]
    print(square(array))