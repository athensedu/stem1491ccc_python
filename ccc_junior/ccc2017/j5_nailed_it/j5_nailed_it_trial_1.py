"""

"""

mylist = [1,2,3,4,5,6,7,10,9,8,12,14,13,16,15,19,18,17]
mylist.sort()
print(mylist)

n = len(mylist)

sum_list = []

# i = 0 ~ n-1
for i in range(n-1):
    print(f'{mylist[i]:2}', end=":  ")
    for j in range(i+1, n):
        print(f'{mylist[j]:2}', end=", ")
        sum_list.append(mylist[i]+mylist[j])
    print()

sum_list.sort()
print(sum_list)

# find fence
sum_map = {}
for item in sum_list:
    sum_map[item] = sum_map.get(item, 0) + 1
print(sum_map)

# find max length of fence
list_key = []
list_value = []
for key,value in sum_map.items():
    list_key.append(key)
    list_value.append(value)
print(list_key)
print(list_value)

# find max
max_length = max(list_value)
count = list_value.count(max_length)
print(max_length)
print(count)




