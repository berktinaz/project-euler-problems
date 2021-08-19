#Project Euler Problem 43 - @Berk Tinaz
import itertools

pandigitals = []

def generate_pandigital(list):
    if (len(list) <= 1):
        return list[0]
    else:
        for i in list:
            temp1 = list
            temp2 = list.remove(i)
            list = temp1
        return [10*i + generate_pandigital(temp2)]



listtemp = list( itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
sum = 0

for i in listtemp:
    if ( (i[1] * 100 + i[2] * 10 + i[3]) % 2 == 0 ):
        if ( (i[2] * 100 + i[3] * 10 + i[4]) % 3 == 0):
            if ( (i[3] * 100 + i[4] * 10 + i[5]) % 5 == 0):
                if ( (i[4] * 100 + i[5] * 10 + i[6]) % 7 == 0):
                    if ( (i[5] * 100 + i[6] * 10 + i[7]) % 11 == 0):
                        if ( (i[6] * 100 + i[7] * 10 + i[8]) % 13 == 0):
                            if ( (i[7] * 100 + i[8] * 10 + i[9]) % 17 == 0):
                                sum += 10**9 * i[0] + 10**8 * i[1] + 10**7 * i[2] + 10**6 * i[3] + 10**5 * i[4] + 10**4 * i[5] + 10**3 * i[6] + 100 * i[7] + 10 * i[8] + i[9]

#pandigitals.append(10**9 * i[0] + 10**8 * i[1] + 10**7 * i[2] + 10**6 * i[3] + 10**5 * i[4] + 10**4 * i[5] + 10**3 * i[6] + 100 * i[7] + 10 * i[8] + i[9])

print(sum)
