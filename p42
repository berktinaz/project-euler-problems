#Project Euler Problem 42 - @Berk Tinaz

words = open("p042words.txt", 'r').read().split(',') #open the 2-thousand word file and split by commas

#initialize variables
myset = []
num = 0

#generate triangle numbers up to 100 elements
for i in range(100):
    myset.append(int(i*(i+1)/2))

#for each word in the text:
#*calculate the corresponding sum
#*check if it is in the generated list
#*if it exists increment the amount
#*else do nothing
for word in words:
    temp_sum = 0
    for char in word:
        if ord(char) > 34:
            temp_sum += ord(char) - 64

    if temp_sum in myset:
        num += 1

print(num)
