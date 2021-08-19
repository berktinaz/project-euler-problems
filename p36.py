def is_palin( num):
    for i in range(len(num)//2):
        if num[i] != num[len(num)-1-i]:
            return False
    return True
 
s = []  
 
for i in range(1000000):
    if is_palin(str(i)) and is_palin( str(bin(i))[2:]):
        s.append(i)
print(s) 
print(sum(s))       