import math
import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(3, int(math.pow(n, 0.5)) + 1, 2):
        if n % i == 0:
            return False
    return True

s_digits = ('2','3','5','7')
o_digits = ('1','3','5','7','9')
e_digits = ('3','7')

generated = []
primes = []
prime = True


def generate( num, count):
    if count == 0:
        return num + ""
    if count == 1:
        for i in range(2):
            generated.append( int(num))
            generate( num + e_digits[i], count - 1)

    else:
        for k in range(5):
            generated.append( int(num))
            generate( num + o_digits[k], count - 1)

start = time.time()
for i in range(4):
    generate( s_digits[i] , 7)

inter = time.time()
print ("intermediate in ", inter - start)
generated = list(set(generated))
for i in range(len(generated)):
    for k in range(len(str(generated[i]))):
        if not (is_prime(int(str(generated[i])[k:]))) or not( is_prime(int(str(generated[i])[:k+1]))):
            prime = False
            break

    if prime:
        primes.append(generated[i])
    prime = True


#for k in range(len(str(primes[16]))):
#    print(int(str(primes[16])[k:]))
print(737 in generated)
print(primes)
print(len(generated))
print(len(primes))
print(sum(primes) - 17)

last = time.time()
print ("last in ", last - start)
