"""

"""
N = int(input())
mylist = input().split()
# mylist.sort()

for i in range(N):
    mylist[i] = int(mylist[i])

n = len(mylist)
sum_list = []

# i = 0 ~ n-1
for i in range(n-1):
    for j in range(i+1, n):
        sum_list.append(mylist[i]+mylist[j])
        mylist[i] = 0
        mylist[j] = 0
# sum_list.sort()


# find fence
sum_map = {}
for item in sum_list:
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




