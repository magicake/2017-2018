#Sahra Yusuf 2018
#github.com/fyusuf1 // fsyusuf1@gmail.com

import math

def main():
    top = int(input("Max: "))
    #print(findFactors(18))
    findSemiprimes(top)

def isPrime(num):
    for i in xrange(2, int(math.sqrt(num-1))):
        if num % i == 0:
            return False
        return True

def primeFactorization(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def isSemiprime(num):
    factors = primeFactorization(num)
    if len(factors) == 1 and factors[0]*factors[0] == num:
        return True
    if len(factors) == 2:
        return True
    return False

def findSemiprimes(top):
    semiprimes = []
    for i in xrange(4, top):
        print(i)
        if isSemiprime(i):
            semiprimes.append(i)
    print(len(semiprimes))

if __name__ == "__main__":
    main()