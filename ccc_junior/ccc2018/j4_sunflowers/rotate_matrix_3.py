"""
zip()
map(list, zip(*matrix))
matrix[::-1]
"""

def outputMatrix(matrix):
    for line in matrix:
        for num in line:
            print(num, end=" ")
        print()

m = [[1,2,3],[4,5,6],[7,8,9]]
outputMatrix(m)
print()

# reverse
m = m[::-1]
outputMatrix(m)
print()

# list
mylist = [1,2,3]
mylist = mylist[::-1]
print(mylist)
print()
