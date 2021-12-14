"""

"""


start = 1200
D = 720
for i in range(D):
    # print(start)
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

num_of_group = [[1200,1259,1],
                [100,159,5],
                [200,259,5],
                [300,359,4],
                [400,459,4],
                [500,559,4],
                [600,659,3],
                [700,759,2],
                [800,859,2],
                [900,959,1],
                [1000,1059,0],
                [1100,1159,1]]

num_of_12_hour = 0
for item in num_of_group:
    num_of_12_hour += item[2]

print(num_of_12_hour)

def getGroupInfo(d):
    round = d // 720
    return round

print(getGroupInfo(720))
