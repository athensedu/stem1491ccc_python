"""

"""
import itertools


def getFullGroup(mylist):
    result = itertools.combinations(mylist,2)
    return list(result)

def getRound(item, my):
    round = []
    used_index = []
    round.append(item)
    used_index.append(item[0])
    used_index.append(item[1])
    mylist = my[:]
    for x in mylist:
        if x[0] not in used_index and x[1] not in used_index:
            round.append(x)
            used_index.append(x[0])
            used_index.append(x[1])
    return round


def getGroupRemovingUsedIndex(mylist):
    allgroup = []
    for x in range(len(mylist)):
        # print(mylist[x])
        a = getRound(mylist[x], mylist)
        a.sort()
        a = tuple(a)
        if a not in allgroup:
            allgroup.append(a)
    return allgroup


# a = [0,1,2,3]
# print(getFullGroup(a))

# print(allCombination)


# fencelist = [1,2,3,4]
N = int(input())
fencelist = input().split()
for i in range(len(fencelist)):
    fencelist[i] = int(fencelist[i])

a = list(range(len(fencelist)))
allCombination = getGroupRemovingUsedIndex(getFullGroup(a))

heights = []
for aCombination in allCombination:
    # print(aCombination)
    for board in aCombination:
        height = fencelist[board[0]]+fencelist[board[1]]
        # print("height = ",height)
        heights.append(height)

# print(heights)

# find fence
sum_map = {}
for item in heights:
    sum_map[item] = sum_map.get(item, 0) + 1
# print(sum_map)


# find max length of fence
# list_key = []
list_value = []
for key,value in sum_map.items():
    if key != 0:
        # list_key.append(key)
        list_value.append(value)

# find max
max_length = max(list_value)
count = list_value.count(max_length)
print(max_length, count)
