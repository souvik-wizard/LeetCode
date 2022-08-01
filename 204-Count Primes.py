# Accepted ans (Using "Sieve of Eratosthenes" approach)
# TC will be O(n log(log n)) becaues of  "harmonic series"   theorm

class Solution:
    def countPrimes(self, n: int) -> int:
        
        primes = [True]*n
        i = 2
        count = 0
        while i*i < n:
            if primes[i]:
                j = i
                while j*i < n:
                    primes[j*i] = False
                    j += 1
            i += 1
        for i in range(2, len(primes)):
            if primes[i]:
                count += 1
        return count




# Brute force  O(n^2)   :(
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
