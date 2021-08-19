import math

def generate_primes():

    primes = []
    sum = 2
    prime = True
    primes.append(2)

    for i in range(3,10000 , 2):
        for j in range(len(primes)):
            if i% primes[j] == 0:
                prime = False
                break
        if prime:
            primes.append(i)
        prime = True
    return primes

def generate_primefactors( num, primes):
    factors = []
    while (num != 1):
        for i in primes:
            if (num == 1):
                break
            if (num % i == 0):
                while( num % i == 0):
                    num = int(num/i)
                if i not in factors:
                    factors.append(i)
                break

    return factors

# A function to print all prime factors of
# a given number n
def primeFactors(n):
    factors = []
    # Print the number of two's that divide n
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):

        # while i divides n , print i ad divide n
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.append(n)

    return factors

factor_len = [0 for i in range(1000000)]
#primes = generate_primes()
print(primeFactors(13254))

for i in range(100000,1000000):
    factor_len[i] = len(primeFactors(i))

for i in range(100000,1000000-3):
    if( factor_len[i] == factor_len[i+1] == factor_len[i+2] == factor_len[i+3] == 4):
        print(i)
        break
