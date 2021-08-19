import sympy

def is_circular( num):
    for i in range(len(str(num))):
        a = str(num)
        if not sympy.isprime(a[i:] + a[:i]):
            return False
    return True
solution = []
for i in range(1000000):
    if is_circular(i):
        solution.append(i)
print(solution)
print(len(solution))