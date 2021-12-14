"""
CCC 2016 Junior
Problem J1. Tournament Selection

status:
"""
N = 6
result = ['X'] * N
for i in range(N):
    result[i] = input()

numWin = result.count('W')
# numLose = N - numWin

if numWin >= 5:
    print(1)
elif numWin >= 3:
    print(2)
elif numWin >= 1:
    print(3)
else:
    print(-1)



