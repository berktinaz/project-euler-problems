def is_pandigital( number):
    for i in range(1,10):
        if str(i) not in number:
            return False
    return True

for i in range(1000):
    if is_pandigital(str(i * 1002003)):
        print(i * 1002003)    
