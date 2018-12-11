#!/usr/bin/python3

import fileinput

gridSize = 300

input = 0
for line in fileinput.input():
    input = int(line.rstrip())

grid = []
for y in range(gridSize):
    rack = []
    for x in range(gridSize):
        cell = ((x+11)*(y+1) + input) * (x+11)
        rack.append(((cell // 100) % 10) - 5)
    grid.append(rack)

sumX = []
for y in range(gridSize):
    row = []
    for x in range(gridSize-2):
        row.append(grid[y][x]+grid[y][x+1]+grid[y][x+2])
    sumX.append(row)

best = -30
bestCoords = (0,0)
sum = []
for y in range(gridSize-2):
    row = []
    for x in range(gridSize-2):
        value = sumX[y][x]+sumX[y+1][x]+sumX[y+2][x]
        row.append(value)
        if value > best:
            best = value
            bestCoords = (x+1, y+1)
    sum.append(row)

print(best)
print(bestCoords)

#1,26
#22,34
