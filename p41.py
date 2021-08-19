def isPandigital( a, digit):
    digits = [i for i in range(1,digit+1)]
    for t in digits:
        if str(t) not in a:
            return False
    if len(a) != digit:
        return False
    return True

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

for i in range(1234567, 7654321):
    if (isPrime(i) and isPandigital(str(i), 7)):
        print(i)
