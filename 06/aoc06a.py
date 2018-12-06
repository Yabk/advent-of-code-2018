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
        if isinstance(map[i][j], int):
            continue
        searchRange = 0
        found = False
        newChar = ''
        while not found:
            searchRange += 1
            for offsetX in range(searchRange+1):
                for offsetY in range(searchRange+1):
                    if offsetX+offsetY !=  searchRange:
                        continue
                    if offsetX+i < len(map):
                        if offsetY+j < len(map[i]):
                            if isinstance(map[i+offsetX][j+offsetY], int):
                                print('found1 '+str(map[i+offsetX][j+offsetY]))
                                if not found:
                                    found = True
                                    newChar = 'c'+str(map[i+offsetX][j+offsetY])
                                else:
                                    if newChar != 'c'+str(map[i+offsetX][j+offsetY]):
                                        newChar = '.'
                        if j-offsetY >= 0 and j > 0:
                            if isinstance(map[i+offsetX][j-offsetY], int):
                                print('found2 ' +str(map[i+offsetX][j-offsetY]))
                                if not found:
                                    found = True
                                    newChar = 'c'+str(map[i+offsetX][j-offsetY])
                                else:
                                    if newChar != 'c'+str(map[i+offsetX][j-offsetY]):
                                        newChar = '.'
                    if i-offsetX >= 0 and i > 0:
                        if offsetY+j < len(map[i]):
                            if isinstance(map[i-offsetX][j+offsetY], int):
                                print('found3 '+str(map[i-offsetX][j+offsetY]))
                                if not found:
                                    found = True
                                    newChar = 'c'+str(map[i-offsetX][j+offsetY])
                                else:
                                    if newChar != 'c'+str(map[i-offsetX][j+offsetY]):
                                        newChar = '.'
                        if j-offsetY >= 0 and j > 0:
                            if isinstance(map[i-offsetX][j-offsetY], int):
                                print('found4 '+str(map[i-offsetX][j-offsetY]))
                                if not found:
                                    found = True
                                    newChar = 'c'+str(map[i-offsetX][j-offsetY])
                                else:
                                    if newChar != 'c'+str(map[i-offsetX][j-offsetY]):
                                        newChar = '.'
        print(searchRange)
        map[i][j] = newChar

for i in range(len(map)):
    print(map[i])

d = {}
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '.':
            continue
        if i == 0 or j == 0 or i == len(map)-1 or j == len(map[i])-1:
            if not isinstance(map[i][j], int):
                d[map[i][j][1:]] = -1
        else:
            if not isinstance(map[i][j], int):
                if map[i][j][1:] in d:
                    if d[map[i][j][1:]] != -1:
                        d[map[i][j][1:]] += 1
                else:
                    d[map[i][j][1:]] = 1

maxNum = 0
for k, v in d.items():
    print(k+' '+str(v))
    if v > maxNum:
        maxNum = v

print(maxNum+1)
