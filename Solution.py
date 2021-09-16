import numpy

n = int(input().split(" ")[0])

matrix = []

for x in range(n):
    row = input().split(" ")
    for y in range(n):
        row[y] = float(row[y])
    matrix.append(row)

result = numpy.linalg.det(matrix)
print(round(result, 2))


