"""
matrix
creating a matrix

by list comprehension
"""

def createMatrix1(m, n):
    N, M = m, n
    # shallow copy
    m = [[]*N] * M
    return m

def createMatrix2(m, n):
    N, M = m, n
    # shallow copy
    m = [[1]*N] * M
    return m

# test
print('Create a matrix - by list comprehension')
print('Shallow copy')
matrix = createMatrix1(4,3)
print(matrix)
print()

print('Shallow copy')
matrix = createMatrix2(4,3)
print(matrix)







