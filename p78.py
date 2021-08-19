import sympy
import eulerlib

memory = [0 for i in range(1000000)]

def numofpartitions( num, sum):
    if num == 0:
        return 1
    if num < 0:
        return 0

    if memory[num] != 0:
        return memory[num]

    for i in range(1, num+1):
        sum += (-1)**(i-1) * ( numofpartitions(int(num - 0.5*i*(3*i-1)), sum) + numofpartitions(int(num - 0.5*i*(3*i+1)), sum))
    memory[num] = sum
    return sum


for j in range(100000):
    temp = numofpartitions(j,0)
    if temp % 1000000 == 0:
        print(str(j) + ": " + str(temp))
        break
