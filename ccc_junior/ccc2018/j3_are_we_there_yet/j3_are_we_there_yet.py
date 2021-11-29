"""

Test case #1:	AC	[0.026s,	9.47 MB]	(0/0)
Test case #2:	AC	[0.025s,	9.47 MB]	(5/5)
Test case #3:	AC	[0.026s,	9.47 MB]	(5/5)
Test case #4:	AC	[0.026s,	9.47 MB]	(5/5)


Resources: 0.103s, 9.47 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (3.0/3 points)
"""

# rawinput = "3 10 12 5"
rawinput = input()
distances = rawinput.split()
N = len(distances)
# print(distances, type(distances))


lines = [[0 for i in range(N)] for j in range(N+1)]
for i in range(N+1):
    # clone the line
    dis = distances[:]
    # convert each item from str to int
    dis = list(map(lambda x: int(x), dis))
    # insert self-to-self distance
    dis.insert(i, 0)
    # lines[i] = dis

    # calculating distance between 2 cities
    for index,v in enumerate(dis):
        if index > i:
            dis[index] = dis[index] + dis[index-1]
    dis.reverse()
    for index,v in enumerate(dis):
        if index > N+1-i:
            dis[index] = dis[index] + dis[index-1]
    dis.reverse()
    # lines[i] = dis

    # output
    line = dis
    for num in line:
        print(num, end=' ')
    print()

# print(lines)



# cities = 'ABCDE'
#
# mylist = [x+y  for x in cities for y in cities]
# print(mylist)

