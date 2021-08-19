#Project Euler Problem 45 - @Berk Tinaz

set1 = []
set2 = []
set3 = []
found = []

for i in range(286,100000):
    set1.append( int(i * (i + 1) / 2) )
    set2.append( int(i * (3 * i - 1) / 2) )
    set3.append( int(i * (2 * i - 1) ) )

for num in set1:
    if num in set2:
        if num in set3:
            found.append(num)
print(found)
