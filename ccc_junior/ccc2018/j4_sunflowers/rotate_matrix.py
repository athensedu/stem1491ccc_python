"""

"""

def rotateLeft(matrix):
    m = matrix
    print("rotate left")
    n = len(m)

    for i in range(n//2):
        for j in range(i, n-1-i):
            matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i], matrix[i][j]
    return m

def rotateRight(matrix):
    m = matrix
    print("rotate right")
    n = len(m)

    for i in range(n//2):
        for j in range(i, n-1-i):
            matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
            matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]

            # matrix[i][j] <= matrix[n-1-j][i]
            # matrix[j][n-1-i] <= matrix[i][j]
            # matrix[n-1-i][n-1-j] <= matrix[j][n-1-i]
            # matrix[n-1-j][i] <= matrix[n-1-i][n-1-j]

    return matrix

def printMatrix(m):
    for row in m:
        print(row)

matrix =[[0,1,2,3,4],
         [9,0,2,3,5],
         [9,8,0,3,6],
         [9,7,6,0,5],
         [6,7,8,9,0]]
printMatrix(matrix)

m = rotateRight(matrix)
printMatrix(m)

m = rotateLeft(matrix)
printMatrix(m)