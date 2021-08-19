#Project Euler Problem 46 - @Berk Tinaz
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

primes = generate_primes()
odds = [0 for i in range(10000000)]
squares = [int(i**2) for i in range(1, 1000)]

for i in squares:
    for j in primes:
        odds[int(j + 2*i)] = 1

for i in range(9,10000,2):
    if( odds[i] == 0 ):
        print(i)
