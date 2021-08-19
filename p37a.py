#!/usr/bin/python

# Problem 37

# The number 3797 has an interesting property. Being prime itself, it
# is possible to continuously remove digits from left to right, and
# remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
# work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def generate_primes( length):

    primes = []
    primes.append(2)

    for i in range(3,10**length , 2):
        for j in range(len(primes)):
            if i% primes[j] == 0:
                break
            primes.append(i)

    return primes

def truncatable( s ):

    a = str(s)
    l = len(a)

    for i in range(l):
        if not is_prime( int(a[i:]) ):
            return False
        if not is_prime( int(a[:i+1]) ):
            return False

    return True


prims = generate_primes( 7)

p = 7
print(prims)
truncatabl = [i for i in prims if truncatable(i)]

print(sum(truncatabl))
