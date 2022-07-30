def countPrimes(n):
    if n < 2:
        return 0
    else:
        count=0
        for i in range(n):    
            for j in range(2, i):
                if i % j == 0:
                    count+=1
                    break
        return count

if __name__=='__main__':
    n=20
    print(countPrimes(n))
