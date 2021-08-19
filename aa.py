#target = 200
#ways = [0]*201
#coins = [1,2,5,10,20,50,100,200]

#for i in range(201):
#    ways.append(0)

#ways[0]= 1
#for i in range(len(coins)):
#    for j in range(coins[i],target+1):
#        ways[j] += ways[j-coins[i]]
#print(ways)


#def is_pandigital( number):
#    for i in range(1,10):
#        if str(i) not in number:
#            return False
#    return True


#print(is_pandigital(str(123456789)))

#solution = [0]*10000

#for i in range(1,100):
#    for j in range(100,10000):
#        if len(str(i)+ str(j)+str(i*j)) == 9 and solution[i*j] != 1 and is_pandigital(str(i)+str(j)+str(i*j)):
#            print(str(i)+ str(j)+str(i*j))
#            solution[i*j] = 1

#suma = 0
#print(solution)
#for i in range(10000):
#    if solution[i] == 1:
#         suma += i
#print(suma)

#q33
#numerator = []
#denominator = []
#for i in range(10,100):
#    for j in range(i+1,100):
#
#        if j%10 != 0 and (i/j) == (i//10)/(j%10) and i%10 == j//10:
#            numerator.append(i)
#            denominator.append(j)
#            print(str(i) + " " + str(j) + str(i/j) + " " + str((i//10)/(j%10)))

#product1 = 1
#for i in numerator:
#    product1 *= i
#product2 = 1
#for i in denominator:
#    product2 *= i
#print(numerator)
#print(str(product1) + "-" + str(product2) )


#q34
#import math
#
#d = {}
#result = []


#for i in range(0,10):
#    d[str(i)] = math.factorial(i)

#for i in range(10,2540160):
#    s = 0
#    a = str(i)
#    for j in range(len(str(i))):
#        s += d[a[j]]
#    if s == i:
#         result.append(i)
#print(sum(result))

import sympy

def is_circular( num):
    for i in range(len(str(num)) - 1):
        a = str(num)
        if not sympy.isprime(a[i:] + a[:i]):
            return False
    return True
solution = []
for i in range(1000000):
    if(is_circular(i)):
        solution.append(i)
print(solution)
