# Accepted ans








# Brute force  O(n^2)
def countPrimes(n):
    arr=[]
    for number in range (n):  
        if number > 1:  
            for i in range (2, number):  
                if (number % i) == 0:  
                    break  
            else:  
                arr.append(number)

    return len(arr)



if __name__=='__main__':
    n=20
    print(countPrimes(n))
