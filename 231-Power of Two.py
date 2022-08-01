import math

def isPowerOfTwo(n):
            if n<=0: return False
            
            # Log functions in Python
            num=math.log2(n)
            if num == int(num):return True
            else: return False
            

if __name__=='__main__':
    n=-2

    print(isPowerOfTwo(n))