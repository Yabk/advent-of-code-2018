#!/usr/bin/python3

import fileinput

coords = []
for line in fileinput.input():
    line = line.rstrip()
    coords.append([int(x) for x in line.split(',')])

minX = coords[0][0]
maxX = coords[0][0]
minY = coords[0][1]
maxY = coords[0][1]
for x, y in coords:
    if x < minX:
        minX = x
    if x > maxX:
        maxX = x
    if y < minY:
        minY = y
    if y > maxY:
        maxY = y

print('minX: '+str(minX)+', maxX: '+str(maxX))
print('minY: '+str(minY)+', maxY: '+str(maxY))
map = []
for i in range(maxX-minX+1):
    map.append(['-']*(maxY-minY+1))

for i in range(len(coords)):
    map[coords[i][0]-minX][coords[i][1]-minY] = i

# for i in range(len(map)):
#     print(map[i])
print(len(map))
for i in range(len(map)):
    for j in range(len(map[i])):
        print()
        print(i, j)
        distances = 0
        for k in range(len(coords)):
            distances += abs(i-coords[k][0]+minX) + abs(j-coords[k][1]+minY)
        if isinstance(map[i][j], int):
            coords[map[i][j]].append(distances)
        else:
            map[i][j] = str(distances)
        print(distances)
for i in range(len(map)):
    print(map[i])

counter = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if not isinstance(map[i][j], int):
            # print()
            # print(i, j)
            # print(map[i][j])
            if int(map[i][j]) < 10000:
                counter += 1
for x, y, dist in coords:
    if dist < 10000:
        counter += 1

print(counter)

#31622
