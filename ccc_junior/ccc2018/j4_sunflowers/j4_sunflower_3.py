"""
Resources: 0.497s, 9.95 MB
Maximum runtime on single test case: 0.031s
Final score: 15/15 (5.0/5 points)
"""

def rotateLeft(matrix):
    # matrix[:] = map(list, zip(*matrix))[::-1]
    matrix[:] = map(list, zip(*matrix))
    return matrix[::-1]

def rotateRight(matrix):
    matrix[:] = map(list, zip(*matrix[::-1]))
    return matrix

def outputMatrix(matrix):
    for line in matrix:
        for num in line:
            print(num, end=" ")
        print()

# main
LEN = int(input())
N = LEN-1

matrix =[[0 for i in range(LEN)] for j in range(LEN)]
for i in range(LEN):
    line = input().split()
    line = list(map(int, line))
    matrix[i] = line

# find the min
a = matrix[0][0]
b = matrix[0][N]
c = matrix[N][0]
d = matrix[N][N]

vertex = min(a,b,c,d)
# print(vertex)

# if the min at left-up corner, stay still
if a == vertex:
    outputMatrix(matrix)

# if the min at right-up corner, rotate left
if b == vertex:
    m = rotateLeft(matrix)
    outputMatrix(m)

# if the min at left-bottom corner, rotate right
if c == vertex:
    m = rotateRight(matrix)
    outputMatrix(m)

# if the min at right-up corner, rotate left or right for twice
if d == vertex:
    m = rotateLeft(rotateLeft(matrix))
    outputMatrix(m)