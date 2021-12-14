"""
matrix
creating a matrix

by nested list
"""

def createMatrix1():
    # direct literal
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return m


def createMatrix2():
    # sublist as item and append
    m = []
    row0 = [1,2,3]
    row1 = [4,5,6]
    row2 = [7,8,9]
    m.append(row0)
    m.append(row1)
    m.append(row2)
    # ERROR:
    # matrix.append(line1).append(line2).append(line3)
    return m

# test
print('Create a matrix - method 1')
matrix = createMatrix1()
print(matrix)
print()

print('Create a matrix - method 2')
matrix = createMatrix2()
print(matrix)
print()






