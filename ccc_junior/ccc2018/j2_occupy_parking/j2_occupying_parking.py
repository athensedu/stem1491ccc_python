"""
Resources: 0.303s, 9.35 MB
Maximum runtime on single test case: 0.025s
Final score: 15/15 (3.0/3 points)
"""

# N = 5
# yesterday = 'CC..C'
# today = '.CC..'

N = int(input())
yesterday = input()[:N]
today = input()[:N]

count = 0
for i, v in enumerate(yesterday):
    # print(i, v)
    if v == 'C' and v == today[i]:
        # print(i)
        count += 1

print(count)