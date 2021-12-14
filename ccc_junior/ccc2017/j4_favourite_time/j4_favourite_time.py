"""
CCC 2017 Junior
Problem J4. Favourite Time

Resources: 0.457s, 9.70 MB
Maximum runtime on single test case: 0.027s
Final score: 15/15 (5.0/5 points)
"""


start = 1200
D_ROUND = 720
LED = [[0,0] for i in range(D_ROUND)]

def isSequence(time):
    strTime = str(time)
    diff_list = []
    for i in range(len(strTime)-1):
        a = int(strTime[i])
        b = int(strTime[i+1])
        diff = b - a
        diff_list.append(diff)

    max_diff = diff_list[0]
    min_diff = max_diff
    for item in diff_list:
        if item > max_diff:
            max_diff = item
        if item < min_diff:
            min_diff = item
    if max_diff == min_diff:
        return 1
    else:
        return 0

for i in range(D_ROUND):
    LED[i][0] = start
    LED[i][1] = isSequence(start)
    start = start + 1
    if start == 1260:
        start = 100
    if start == 160:
        start = 200
    if start == 260:
        start = 300
    if start == 360:
        start = 400
    if start == 460:
        start = 500
    if start == 560:
        start = 600
    if start == 660:
        start = 700
    if start == 760:
        start = 800
    if start == 860:
        start = 900
    if start == 960:
        start = 1000
    if start == 1060:
        start = 1100
    if start == 1160:
        start = 1200


# SUM_D_ROUND = 31
sum = 0
for item in LED:
    sum += item[1]

def countRemainder(n):
    sum = 0
    for i in range(n+1):
        sum += LED[i][1]
    return sum


D = int(input())
part1 = D//720 * sum
part2 = countRemainder(D%720)

result = part1 + part2
print(result)


