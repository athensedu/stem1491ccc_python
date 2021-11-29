"""

"""

def rotateLeft(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-1-i):
            matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i], matrix[i][j]
    return matrix

def rotateRight(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-1-i):
            matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
    return matrix

def outputMatrix(matrix):
    for line in matrix:
        for num in line:
            print(num, end=" ")
        print()


# main
LEN = int(input())
N = LEN-1

matrix =[]
for i in range(LEN):
    matrix.append(input().split())

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