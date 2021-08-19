import sympy

def generate_primes():

    primes = []
    sum = 2
    prime = True
    primes.append(2)

    for i in range(3,100000 , 2):
        if sum < 1000000:
            for j in range(len(primes)):
                if i% primes[j] == 0:
                    prime = False
                    break
            if prime:
                primes.append(i)
                sum += i
            prime = True
        else:
            break
    return primes, sum

primes, sum = generate_primes()
print(primes)
print(sum)
print(len(primes))
tempsum = 0

for i in range(len(primes)):
    tempsum += primes[i]

print(tempsum)

sum -= primes[len(primes)-1]
primes.remove(primes[len(primes)-1])

while sum >= 0:
    if sympy.isprime(sum) and sum < 1000000:
        print(sum)
        break
    else:
        sum = sum - primes[0]
        primes.remove(primes[0])
        print(primes)
        print(sum)
