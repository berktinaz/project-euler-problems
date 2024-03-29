#Project Euler Problem 44 - @Berk Tinaz
#Project Euler Problem 44
def pe44():
    ps = set()
    i = 1000
    while True:
        i += 1
        s = (3*i*i - i) // 2
        for Pj in ps:
            if s-Pj in ps and s-2*Pj in ps:
                return s-2*Pj
        ps.add(s)

print("Project Euler 44 Solution =", pe44())
