"""
CCC 2016 Junior
Problem J4. Arrival Time

status:

"""

# distance per 10 min not-in-rush-time
DistanceUnit = 2
# distance per 10 min in-rush-time
HalfDistanceUnit = 1

# filling with Distance
timeSlots = [str(h)+":"+str(mm).zfill(2) for h in range(24) for mm in range(0, 60, 10)]
print(timeSlots)
distanceSlot = [DistanceUnit for h in range(24) for mm in range(0, 60, 10) ]
print(distanceSlot)

# Total Distance
Distance = 2 * 60 //10 * DistanceUnit
print(Distance)

startTime = '9:00'
travelledDistance = 0
index = timeSlots.index(startTime)

while travelledDistance < Distance:
    travelledDistance += distanceSlot[index]
    print(travelledDistance)
    index+=1

print('index',index)
print('timeSlots',timeSlots[index])
