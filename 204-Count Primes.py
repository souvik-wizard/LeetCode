# # Accepted ans (Using "Sieve of Eratosthenes" approach)
# # TC will be O(n log(log n)) becaues of  "harmonic series"   theorm

import math
def countPrimes(n):
    if n<=1:
        return 0
    prime=[True]*n        
    prime[0]=False
    prime[1]=False        
    for i in range(2,math.ceil(n**0.5)):
        if prime[i]:
            for j in range(i*i,n,i):
                prime[j]=False
                
    return len([i for i in range(n) if prime[i]])
                    


# # Brute force  O(n^2)Thats y not accepted   :(

# def countPrimes(n):
#     arr=[]
#     for number in range (n):  
#         if number > 1:  
#             for i in range (2, number):  
#                 if (number % i) == 0:  
#                     break  
#             else:  
#                 arr.append(number)
#         else:
#             return 0

#     return len(arr)





if __name__=='__main__':
    n=10000
    print(countPrimes(n))
