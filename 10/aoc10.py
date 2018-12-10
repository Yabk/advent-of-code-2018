#!/usr/bin/python3

import fileinput
import re

positions = []
velocities = []
for line in fileinput.input():
    line = line.rstrip()
    split = re.split(r'[<,>]', line)
    positions.append([int(split[1]), int(split[2])])
    velocities.append((int(split[4]), int(split[5])))

iter = 0
while True:
    iter += 1

    for i in range(len(positions)):
        positions[i][0] += velocities[i][0]
        positions[i][1] += velocities[i][1]

    xVals = [pos[0] for pos in positions]
    minX = min(xVals)
    maxX = max(xVals)
    if maxX - minX > 100:
        continue
    yVals = [pos[1] for pos in positions]
    minY = min(yVals)
    maxY = max(yVals)
    if maxY - minY > 100:
        continue

    canvas = []
    for i in range(maxY-minY+1):
        canvas.append(['.']*(maxX-minX+1))
    offsetX = minX
    offsetY = minY
    for i in range(len(positions)):
        canvas[positions[i][1]-offsetY][positions[i][0]-offsetX] = '#'

    for line in canvas:
        print(''.join(line))

    print(iter)
