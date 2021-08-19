matrix = []

with open("p081_matrix.txt") as textFile:
        lines = [[int(x) for x in line.strip().split(",")] for line in textFile]

print(lines)
for i in range(79):
    lines[79][78-i] = lines[79][79-i] + lines[79][78-i]
    lines[78-i][79] = lines[79-i][79] + lines[78-i][79]

for i in range(1,80):
    for j in range(1, 80):
        lines[79-i][79-j] = lines[79-i][79-j] + min( lines[80-i][79-j], lines[79-i][80-j])


print(lines[0][0])
