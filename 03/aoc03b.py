#!/usr/bin/python3

import fileinput

fabric = [  [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

possible = []

def resize(fabric, width, height):
    if width > len(fabric[0]):
        current = len(fabric[0])
        iter = width - current + 1
        for line in fabric:
            for i in range(iter):
                line.append(0)

    if height > len(fabric):
        current = len(fabric)
        iter = height - current + 1
        wid = max(width, len(fabric[0]))
        for i in range(iter):
            fabric.append([0]*wid)

for line in fileinput.input():
    line = line.rstrip()

    split = line.split()
    coor = split[2].split(',')
    x = int(coor[0])
    y = int(coor[1].split(':')[0])

    size = split[3].split('x')
    width = int(size[0])
    height = int(size[1])

    resize(fabric, x+width, y+height)

    poss = True
    for i in range(y, y+height):
        for j in range(x, x+width):
            fabric[i][j] += 1
            if fabric[i][j] > 1:
                poss = False
    if poss:
        possible.append( (int(split[0][1:]), int(x), int(y), int(width), int(height)))

counter = 0
for line in fabric:
    for num in line:
        if num > 1:
            counter += 1

print(counter)
print(len(fabric))
print(len(fabric[0]))
print(len(possible))

for line in possible:
    dobar = True
    x = line[1]
    y = line[2]
    width = line[3]
    height = line[4]
    for i in range(y, y+height):
        if dobar:
            for j in range(x, x+width):
                if fabric[i][j] > 1:
                    dobar = False
                    break
    if dobar:
        print(line[0])
